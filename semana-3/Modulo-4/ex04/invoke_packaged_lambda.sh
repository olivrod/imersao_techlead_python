#!/bin/bash

aws lambda invoke \
  --function-name packaged_lambda \
  --cli-binary-format raw-in-base64-out \
  --payload '{}' \
  --endpoint-url http://localhost:4566 \
  response.json

cat response.json