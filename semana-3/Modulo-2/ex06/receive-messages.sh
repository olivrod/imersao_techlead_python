#!/bin/bash
# receives up to 3 messages from queue '42sp-${whoami}-queue'
whoami=$(whoami)
aws sqs receive-message --queue-url "http://localhost:4566/000000000000/42sp-${whoami}-queue" --max-number-of-messages 3 --region us-east-1 --endpoint-url http://localhost:4566
