#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3api create-bucket --bucket $BUCKET --region us-east-1
aws --endpoint-url=$ENDPOINT_URL s3api wait bucket-exists --bucket $BUCKET

echo "Bucket $BUCKET criado com sucesso."

BUCKET="42sp-rde-oliv-bucket-converted"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3api create-bucket --bucket $BUCKET --region us-east-1
aws --endpoint-url=$ENDPOINT_URL s3api wait bucket-exists --bucket $BUCKET

echo "Bucket $BUCKET criado com sucesso."