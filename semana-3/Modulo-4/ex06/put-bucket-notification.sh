#!/bin/bash

LOGIN="rde-oliv"
BUCKET="42sp-$LOGIN-bucket"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3api put-bucket-notification-configuration \
  --bucket $BUCKET \
  --notification-configuration file://notification.json

echo "Notificação configurada para o bucket $BUCKET."