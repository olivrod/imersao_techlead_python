#!/bin/bash

aws lambda invoke \
  --function-name first_lambda \
  --payload '{}' \
  --endpoint-url http://localhost:4566 \
  response.json

cat response.json