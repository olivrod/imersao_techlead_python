#!/bin/bash
# list aws sqs queue with name '42sp-${whoami}-queue'
aws sqs list-queues --region us-east-1 --endpoint-url http://localhost:4566