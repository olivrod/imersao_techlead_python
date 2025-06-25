#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"
ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3 ls s3://$BUCKET/