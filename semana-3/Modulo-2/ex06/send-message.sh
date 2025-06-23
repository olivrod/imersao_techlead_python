#!/bin/bash
# send message to queue '42sp-${whoami}-queue'
whoami=$(whoami)
aws sqs send-message --queue-url "http://localhost:4566/000000000000/42sp-${whoami}-queue" --message-body "Olá SQS" --region us-east-1 --endpoint-url http://localhost:4566
