#!/bin/bash

LOGIN="rde-oliv"
BUCKET="42sp-$LOGIN-bucket2"
BUCKET_CONVERTED="42sp-$LOGIN-bucket-converted"

# Cria os buckets (ignora erro se já existem)
# aws --endpoint-url=http://localhost:4566 s3 mb s3://$BUCKET
# aws --endpoint-url=http://localhost:4566 s3 mb s3://$BUCKET_CONVERTED

# Prepara o pacote com Pillow
rm -rf package package.zip
mkdir -p package
docker run --rm -v "$PWD":/var/task \
  --entrypoint /bin/sh \
  public.ecr.aws/lambda/python:3.13 \
  -c "pip install pillow -t package/"
cp lambda_convert.py package/
(cd package && zip -r ../package.zip .)

# Remove função se já existir
aws lambda delete-function --function-name lambda_convert --region us-east-1 2>/dev/null

# Remove permissão se já existir
aws lambda remove-permission --function-name lambda_convert --statement-id s3invoke --region us-east-1 2>/dev/null


# Cria a função Lambda
aws lambda create-function \
  --function-name lambda_convert \
  --handler lambda_convert.lambda_handler \
  --zip-file fileb://package.zip \
  --runtime python3.13 \
  --role arn:aws:iam::452807283394:role/D04-LambdaS3AccessRole \
  --region us-east-1 \
  --no-cli-pager

# Adiciona permissão para o S3 invocar a função Lambda
aws lambda add-permission \
  --function-name lambda_convert \
  --action lambda:InvokeFunction \
  --statement-id s3invoke \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::$BUCKET \
  --region us-east-1

aws lambda add-permission \
  --function-name lambda_convert \
  --action lambda:InvokeFunction \
  --statement-id s3invoke \
  --principal s3.amazonaws.com \
  --source-arn arn:aws:s3:::$BUCKET_CONVERTED \
  --region us-east-1

# Limpa arquivos temporários
rm -rf package package.zip