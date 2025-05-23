#!/bin/bash

Carrega variáveis do .env,
export $(grep -v '^#' .env | xargs)

NETWORK_NAME=my_network
DB_CONTAINER_NAME=my_postgres
APP_CONTAINER_NAME=minha_api
DB_IMAGE=postgres:16
APP_IMAGE=minha_api
APP_PORT=8080

Cria rede,
docker network create $NETWORK_NAME || echo "Rede já existe."

Subindo o banco de dados,
docker run -d \
  --name $DB_CONTAINER_NAME \
  --network $NETWORK_NAME \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  -p $POSTGRES_PORT:5432 \
  $DB_IMAGE

Aguarda o banco subir,
sleep 5

Build,
docker build -t $APP_IMAGE .

Subindo app,
docker run -d \
  --name $APP_CONTAINER_NAME \
  --network $NETWORK_NAME \
  -e POSTGRES_USER=$POSTGRES_USER \
  -e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
  -e POSTGRES_DB=$POSTGRES_DB \
  -e POSTGRES_HOST=$DB_CONTAINER_NAME \
  -e POSTGRES_PORT=$POSTGRES_PORT \
  -p $APP_PORT:8080 \
  $APP_IMAGE