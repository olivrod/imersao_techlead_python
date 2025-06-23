#!/bin/bash
# create aws sqs queue with name '42sp-${whoami}-queue'
whoami=$(whoami)
aws sqs create-queue --queue-name "42sp-${whoami}-queue" --attributes '{"DelaySeconds":"0","MessageRetentionPeriod":"86400"}' --region us-east-1 --endpoint-url http://localhost:4566
