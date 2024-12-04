resource "aws_iam_role" "lambda-role" {
  name               = "lambda-exec-role"
  assume_role_policy = <<POLICY
{
   "Version":"2012-10-17",
   "Statement":{
      "Action":"sts:AssumeRole",
      "Principal":{
         "Service":"lambda.amazonaws.com"
      },
      "Effect":"Allow"
   }
}
POLICY
}

resource "aws_iam_role_policy" "lambda_ecr_permissions" {
  name = "lambda-ecr-policy"
  role = aws_iam_role.lambda-role.id

  policy = <<POLICY
   {
      "Version": "2012-10-17",
      "Statement": [
         {
            "Effect": "Allow",
            "Action": [
               "logs:CreateLogGroup",
               "logs:CreateLogStream",
               "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
         },
         {
            "Effect": "Allow",
            "Action": [
               "ecr:GetAuthorizationToken",
               "ecr:BatchCheckLayerAvailability",
               "ecr:PutImage",
               "ecr:InitiateLayerUpload",
               "ecr:UploadLayerPart",
               "ecr:CompleteLayerUpload"
            ],
            "Resource": "*"
         },
         {
            "Effect": "Allow",
            "Action": [
               "lambda:InvokeFunction"
            ],
            "Resource": "*"
         },
         {
            "Effect": "Allow",
            "Action": [
   	      	"dynamodb:DescribeImport",
   	      	"dynamodb:DescribeContributorInsights",
   	      	"dynamodb:ListTagsOfResource",
   	      	"logs:CreateLogStream",
   	      	"dynamodb:DescribeTable",
   	      	"dynamodb:PartiQLSelect",
   	      	"dynamodb:GetItem",
   	      	"dynamodb:DescribeContinuousBackups",
   	      	"dynamodb:DescribeExport",
   	      	"dynamodb:DescribeKinesisStreamingDestination",
   	      	"dynamodb:GetResourcePolicy",
   	      	"dynamodb:BatchGetItem",
   	      	"dynamodb:ConditionCheckItem",
   	      	"dynamodb:PutItem",
   	      	"dynamodb:Scan",
   	      	"dynamodb:DescribeStream",
   	      	"dynamodb:Query",
   	      	"dynamodb:DescribeTimeToLive",
   	      	"logs:CreateLogGroup",
   	      	"logs:PutLogEvents",
   	      	"dynamodb:DescribeGlobalTableSettings",
   	      	"dynamodb:DescribeGlobalTable",
   	      	"dynamodb:GetShardIterator",
   	      	"dynamodb:DescribeBackup",
   	      	"dynamodb:DescribeTableReplicaAutoScaling",
   	      	"dynamodb:GetRecords"
   	      ],
   	      "Resource": [
   	      	"arn:aws:logs:*:*:*",
   	      	"arn:aws:dynamodb:us-east-1:334325648084:table/magneto-dna-data"
   	      ]
         },
         {
            "Effect": "Allow",
            "Action": [
              "logs:CreateLogGroup",
              "logs:CreateLogStream",
              "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
         }
      ]
   }
   POLICY
}


output "lambda_role_arn" {
  value = aws_iam_role.lambda-role.arn
}

output "iam_role_arn" {
  value = aws_iam_role.lambda-role.arn

}
