#!/bin/bash

LAMBDA_NAME="secret_token"

aws lambda invoke --function-name $LAMBDA_NAME --cli-binary-format raw-in-base64-out --payload '{"token": "secret"}' response.json

echo "Response from Lambda function:"
cat response.json | jq '{StatusCode: .StatusCode, ExecutedVersion: .ExecutedVersion}'