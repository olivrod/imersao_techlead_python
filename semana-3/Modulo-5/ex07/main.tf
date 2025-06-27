terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
#terraform apply -var "lambda_role=arn:aws:iam::697441478992:role/D05-LambdaS3DynamoAccessRole"
# Configure the AWS Provider
provider "aws" {}

resource "aws_s3_bucket" "bucket" {
    bucket = "42sp-rde-oliv-boletos"
}

resource "aws_sqs_queue" "queue" {
    name = "42sp-rde-oliv-queue"
}

resource "aws_sqs_queue_policy" "sqs_policy" {
    queue_url = aws_sqs_queue.queue.id
    policy    = jsonencode({
        "Version": "2012-10-17",
        "Id": "example-ID",
        "Statement": [
            {
                "Sid": "example-statement-ID",
                "Effect": "Allow",
                "Principal": {
                    "Service": "s3.amazonaws.com"
                },
                "Action": [
                    "SQS:SendMessage"
                ],
                "Resource": "${aws_sqs_queue.queue.arn}",
                "Condition": {
                    "ArnLike": {
                        "aws:SourceArn": "arn:aws:s3:*:*:42sp-rde-oliv-boletos"
                    },
                    "StringEquals": {
                        "aws:SourceAccount": "697441478992"
                    }
                }
            }
        ]
    })
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.bucket.id

  queue {
    queue_arn     = aws_sqs_queue.queue.arn
    events        = ["s3:ObjectCreated:*"]
  }
}

# Package the Lambda function code
data "archive_file" "example" {
    type        = "zip"
    source_file = "${path.module}/../ex04/processa_boletos_lambda.py"
    output_path = "${path.module}/lambda.zip"
}

variable "lambda_role"{
    type = string
}

# Lambda function
resource "aws_lambda_function" "example" {
    filename         = data.archive_file.example.output_path
    function_name    = "processa_boletos_lambda"
    role             = var.lambda_role
    handler          = "processa_boletos_lambda.lambda_handler"
    source_code_hash = data.archive_file.example.output_base64sha256
    timeout = 30
    runtime = "python3.13"
}

resource "aws_lambda_event_source_mapping" "example" {
  event_source_arn = aws_sqs_queue.queue.arn
  function_name    = aws_lambda_function.example.arn
}