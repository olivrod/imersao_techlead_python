#!/bin/bash
# filepath: /nfs/homes/rde-oliv/Imersao TechLead/semana-3/upload_object.sh

BUCKET="42sp-rde-oliv-bucket"
FILE="meuarquivo.txt"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3 cp $FILE s3://$BUCKET/
echo "Arquivo $FILE enviado para o bucket $BUCKET."