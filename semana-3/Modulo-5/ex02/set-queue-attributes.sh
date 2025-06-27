aws sqs set-queue-attributes \
    --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/42sp-MATHERIB-queue \
    --attributes file://sqs_policy.json

#aws sqs get-queue-attributes --queue-url http://sqs.us-east-1.localhost.localstack.cloud:4566/000000000000/42sp-MATHERIB-queue --attribute-names Policy --no-cli-pager