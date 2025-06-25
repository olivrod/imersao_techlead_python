#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3api put-bucket-notification-configuration \
  --bucket $BUCKET \
  --notification-configuration file://notification.json

echo "Notificação configurada para o bucket $BUCKET."