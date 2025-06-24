#!/bin/bash

ENDPOINT_URL="http://localhost:4566"

echo "Criando a tabela DynamoDB..."
aws dynamodb create-table \
    --cli-input-json file://table_config.json \
    --endpoint-url $ENDPOINT_URL \
    --region us-east-1 \
    --no-cli-pager

echo "Aguardando a tabela estar ativa..."
aws dynamodb wait table-exists \
    --table-name Usuarios \
    --endpoint-url $ENDPOINT_URL \
    --region us-east-1 \
    --no-cli-pager

echo "Tabela criada com sucesso."

# source ../../dev.env
# aws dynamodb delete-table --table-name Usuarios --endpoint-url http://localhost:4566 --no-cli-pager
# aws dynamodb describe-table --table-name Usuarios --endpoint-url http://localhost:4566 --no-cli-pager
# aws dynamodb wait help --no-cli-pager