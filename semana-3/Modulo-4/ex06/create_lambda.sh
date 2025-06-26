#!/bin/bash

LOGIN="rde-oliv"
BUCKET="42sp-$LOGIN-bucket"
BUCKET_CONVERTED="42sp-$LOGIN-bucket-converted"

# Cria os buckets (ignora erro se já existem)
aws --endpoint-url=http://localhost:4566 s3 mb s3://$BUCKET
aws --endpoint-url=http://localhost:4566 s3 mb s3://$BUCKET_CONVERTED

# Prepara o pacote com Pillow
rm -rf package package.zip
mkdir -p package
docker run --rm -v "$PWD":/var/task \
  --entrypoint /bin/sh \
  public.ecr.aws/lambda/python:3.13 \
  -c "pip install pillow -t package/"
cp lambda_convert.py package/
(cd package && zip -r ../package.zip .)

# Cria a função Lambda
aws lambda delete-function --function-name lambda_convert --endpoint-url http://localhost:4566 2>/dev/null

aws lambda create-function \
  --function-name lambda_convert \
  --handler lambda_convert.lambda_handler \
  --zip-file fileb://package.zip \
  --runtime python3.13 \
  --role arn:aws:iam::000000000000:role/lambda-role \
  --endpoint-url http://localhost:4566 \
  --no-cli-pager

# Limpa arquivos temporários
rm -rf package package.zip