resource "aws_api_gateway_rest_api"  "magneto_api" {
  name          = "magneto-api-${var.environment_name}"
}

resource "aws_api_gateway_resource" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.magneto_api.id
  parent_id   = aws_api_gateway_rest_api.magneto_api.root_resource_id
  path_part   = "{proxy+}"
}

resource "aws_api_gateway_method" "proxy" {
  rest_api_id   = aws_api_gateway_rest_api.magneto_api.id
  resource_id   = aws_api_gateway_resource.proxy.id
  http_method   = "ANY"
  authorization = "NONE"
  api_key_required = false
}

resource "aws_api_gateway_integration" "lambda_integration" {
  rest_api_id             = aws_api_gateway_rest_api.magneto_api.id
  resource_id             = aws_api_gateway_resource.proxy.id
  http_method             = aws_api_gateway_method.proxy.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = var.invoke_arn
}


resource "aws_api_gateway_method" "proxy_root" {
  rest_api_id   = "${aws_api_gateway_rest_api.magneto_api.id}"
  resource_id   = "${aws_api_gateway_rest_api.magneto_api.root_resource_id}"
  http_method   = "ANY"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "lambda_root" {
  rest_api_id = "${aws_api_gateway_rest_api.magneto_api.id}"
  resource_id = "${aws_api_gateway_method.proxy_root.resource_id}"
  http_method = "${aws_api_gateway_method.proxy_root.http_method}"

  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = var.invoke_arn
}


# resource "aws_api_gateway_method_response" "proxy" {
#   rest_api_id = aws_api_gateway_rest_api.magneto_api.id
#   resource_id = aws_api_gateway_resource.proxy.id
#   http_method = aws_api_gateway_method.proxy.http_method
#   status_code = "200"
# }

# resource "aws_api_gateway_integration_response" "proxy" {
#   rest_api_id = aws_api_gateway_rest_api.magneto_api.id
#   resource_id = aws_api_gateway_resource.proxy.id
#   http_method = aws_api_gateway_method.proxy.http_method
#   status_code = aws_api_gateway_method_response.proxy.status_code

#   depends_on = [
#     aws_api_gateway_method.proxy_root,
#     aws_api_gateway_integration.lambda_integration
#   ]
# }

resource "aws_api_gateway_deployment" "gw_deployment" {
  depends_on = [
    "aws_api_gateway_integration.lambda_integration",
    "aws_api_gateway_integration.lambda_root",
  ]
  rest_api_id = aws_api_gateway_rest_api.magneto_api.id
  stage_name  = var.environment_name
}

output "base_url" {
  value = "${aws_api_gateway_deployment.gw_deployment.invoke_url}"
}

output "api_gateway_execution_arn" {
  value = aws_api_gateway_rest_api.magneto_api.execution_arn
}