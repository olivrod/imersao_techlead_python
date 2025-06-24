#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
FILE="meuarquivo.txt"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3 rm s3://$BUCKET/$FILE
echo "Arquivo $FILE removido do bucket $BUCKET."