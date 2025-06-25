#!/bin/bash

# Cria o diretório package e instala a dependência
mkdir -p package
docker run --rm -v "$PWD":/var/task \
  --entrypoint /bin/sh \
  public.ecr.aws/lambda/python:3.13 \
  -c "pip install pillow -t package/"

# Copia o código da lambda para o package
cp packaged_lambda.py package/

# Cria o zip
(cd package && zip -r ../package.zip .)

# Cria a função Lambda no Localstack
aws lambda create-function \
  --function-name packaged_lambda \
  --handler packaged_lambda.lambda_handler \
  --zip-file fileb://package.zip \
  --runtime python3.13 \
  --role arn:aws:iam::000000000000:role/lambda-role \
  --endpoint-url http://localhost:4566 \
  --no-cli-pager

# Limpa arquivos temporários
rm -rf package package.zip