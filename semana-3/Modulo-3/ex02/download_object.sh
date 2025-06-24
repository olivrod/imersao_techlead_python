#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"

# ex02
FILE="meuarquivo.txt"
# ex03
# FILE="image1.jpg"
# ex06
# FILE="d082af46-130f-4236-9812-31ca909c7f4a.jpg"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3 cp s3://$BUCKET/$FILE ./download/
echo "Arquivo $FILE baixado do bucket $BUCKET."