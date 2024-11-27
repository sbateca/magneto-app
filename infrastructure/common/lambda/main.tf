resource "aws_lambda_function" "backend" {
  image_uri     = "${var.image_uri}@${var.image_tag}"
  package_type = "Image"
  memory_size = var.memory_size
  timeout = var.timeout
  architectures = ["x86_64"]
  function_name = "backend-lambda-function-${var.environment_name}"
  role          = var.lambda_role_arn
}

resource "aws_lambda_function_url" "backend_url" {
  function_name = aws_lambda_function.backend.function_name
  authorization_type = "NONE"
  cors {
    allow_origins = ["*"]
    allow_methods = ["GET", "POST"]
    allow_headers = ["*"]
  }
}

resource "aws_lambda_permission" "permission" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.backend.function_name}"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${var.api_gateway_execution_arn}/*/*"
}

output "lambda_invoke_arn" {
  value = aws_lambda_function.backend.invoke_arn
}