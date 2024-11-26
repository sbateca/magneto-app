module "lambda" {
  source           = "./common/lambda"
  environment_name = local.environment_name
  lambda_role_arn  = module.iam.lambda_role_arn
  region           = local.region
  image_uri        = var.image_uri
  image_tag        = var.image_tag
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