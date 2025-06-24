#!/bin/bash
# filepath: /nfs/homes/rde-oliv/Imersao TechLead/semana-3/list_buckets.sh

ENDPOINT_URL="http://localhost:4566"

aws --endpoint-url=$ENDPOINT_URL s3api list-buckets --query "Buckets[].Name"