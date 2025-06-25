#!/bin/bash

BUCKET="42sp-rde-oliv-bucket"

aws s3api get-bucket-policy --bucket $BUCKET --query Policy --output text | jq .