#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
FILE="ea2be563-8364-4b33-8728-f81ed9be6dd3.jpg"

# Garante que o diretório de download existe
mkdir -p ./download

# Baixa o arquivo do bucket na AWS real
aws s3 cp s3://$BUCKET/$FILE ./download/
echo "Arquivo $FILE baixado do bucket $BUCKET."