module "lambda" {
  source                    = "./common/lambda"
  environment_name          = local.environment_name
  lambda_role_arn           = module.iam.lambda_role_arn
  region                    = local.region
  image_uri                 = module.ecr.ecr_url
  image_tag                 = local.image_tag
  api_gateway_execution_arn = module.gateway.api_gateway_execution_arn
}

module "gateway" {
  source           = "./common/gateway"
  environment_name = local.environment_name
  invoke_arn       = module.lambda.lambda_invoke_arn
}

module "iam" {
  source           = "./common/iam"
  region           = local.region
  environment_name = local.environment_name
}

module "ecr" {
  source        = "./common/ecr"
  ecr_repo_name = format("%s-%s-%s", local.app_name, "ecr", local.environment_name)
}

module "dynamo_db" {
  source         = "./common/dynamo_db"
  dna_table_name = local.dna_table_name
}