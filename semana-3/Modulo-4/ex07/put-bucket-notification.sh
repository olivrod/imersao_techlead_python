#!/bin/bash

LOGIN="rde-oliv"
BUCKET="42sp-$LOGIN-bucket2"
ENDPOINT_URL="http://localhost:4566"

aws s3api put-bucket-notification-configuration \
  --bucket $BUCKET \
  --notification-configuration file://notification.json \
  --region us-east-1

echo "Notificação configurada para o bucket $BUCKET."