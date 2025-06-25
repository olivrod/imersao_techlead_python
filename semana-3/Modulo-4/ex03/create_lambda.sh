#!/bin/bash

zip first_lambda.zip first_lambda.py

aws lambda create-function \
  --function-name first_lambda \
  --handler first_lambda.lambda_handler \
  --zip-file fileb://first_lambda.zip \
  --runtime python3.13 \
  --role arn:aws:iam::000000000000:role/lambda-role \
  --endpoint-url http://localhost:4566 \
  --no-cli-pager

aws lambda get-function \
    --function-name first_lambda \
    --endpoint-url http://localhost:4566 \
    --no-cli-pager