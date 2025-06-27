echo Criando a tabela DynamoDB...

aws dynamodb create-table --cli-input-json file://table_config.json --no-cli-pager

echo Aguardando a tabela estar ativa...

aws dynamodb wait table-exists --table-name Boletos

echo Tabela criada com sucesso