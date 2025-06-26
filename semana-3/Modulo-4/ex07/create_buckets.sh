#!/bin/bash

BUCKET="42sp-rde-oliv-bucket2"
aws s3 mb s3://$BUCKET --region us-east-1
echo "Bucket $BUCKET criado com sucesso."

BUCKET="42sp-rde-oliv-bucket-converted"
aws s3 mb s3://$BUCKET --region us-east-1
echo "Bucket $BUCKET criado com sucesso."