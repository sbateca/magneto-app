resource "aws_api_gateway_rest_api" "magneto_api" {
  name = "magneto-api-${var.environment_name}"
}

resource "aws_api_gateway_resource" "get_path" {
  rest_api_id = aws_api_gateway_rest_api.magneto_api.id
  parent_id   = aws_api_gateway_rest_api.magneto_api.root_resource_id
  path_part   = "GET"
}

resource "aws_api_gateway_method" "get_path_method" {
  rest_api_id   = aws_api_gateway_rest_api.magneto_api.id
  resource_id   = aws_api_gateway_resource.get_path.id
  http_method   = "GET"
  authorization = "NONE"
  api_key_required = false
}

resource "aws_api_gateway_integration" "get_path_integration" {
  rest_api_id             = aws_api_gateway_rest_api.magneto_api.id
  resource_id             = aws_api_gateway_resource.get_path.id
  http_method             = aws_api_gateway_method.get_path_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = var.invoke_arn
}

resource "aws_api_gateway_resource" "mutant_path" {
  rest_api_id = aws_api_gateway_rest_api.magneto_api.id
  parent_id   = aws_api_gateway_rest_api.magneto_api.root_resource_id
  path_part   = "mutant"
}

resource "aws_api_gateway_method" "mutant_path_method" {
  rest_api_id   = aws_api_gateway_rest_api.magneto_api.id
  resource_id   = aws_api_gateway_resource.mutant_path.id
  http_method   = "POST"
  authorization = "NONE"
  api_key_required = false
}

resource "aws_api_gateway_integration" "mutant_path_integration" {
  rest_api_id             = aws_api_gateway_rest_api.magneto_api.id
  resource_id             = aws_api_gateway_resource.mutant_path.id
  http_method             = aws_api_gateway_method.mutant_path_method.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = var.invoke_arn
}

resource "aws_api_gateway_deployment" "gw_deployment" {
  depends_on = [
    aws_api_gateway_integration.get_path_integration,
    aws_api_gateway_integration.mutant_path_integration,
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
