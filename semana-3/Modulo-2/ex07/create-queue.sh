#!/bin/bash
# create aws sqs queue FIFO with name '42sp-${whoami}-queue' with at-least-once delivery and exactly-once processing to avoid duplicates
whoami=$(whoami)
aws sqs create-queue --queue-name "42sp-${whoami}-queue.fifo" --attributes '{"FifoQueue":"true","ContentBasedDeduplication":"true","DelaySeconds":"0","MessageRetentionPeriod":"86400"}' --region us-east-1 --endpoint-url http://localhost:4566
