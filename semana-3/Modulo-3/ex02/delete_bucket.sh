#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
ENDPOINT_URL="http://localhost:4566"

# Remove todos os objetos do bucket antes de deletar
aws --endpoint-url=$ENDPOINT_URL s3 rm s3://$BUCKET --recursive

# Deleta o bucket
aws --endpoint-url=$ENDPOINT_URL s3api delete-bucket --bucket $BUCKET

echo "Bucket $BUCKET removido com sucesso."