#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"

# Remove o bloqueio de acesso público
aws s3api delete-public-access-block --bucket $BUCKET

# Aplica a política pública de leitura
aws s3api put-bucket-policy --bucket $BUCKET --policy file://policy.json

echo "Policy aplicada ao bucket."