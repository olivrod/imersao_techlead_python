#!/bin/bash

# Cria a rede se ainda não existir
docker network inspect ningipoints-network >/dev/null 2>&1 || \
docker network create ningipoints-network

# Sobe o container do banco de dados, se ainda não estiver rodando
docker ps -a | grep ningipoints-postgres >/dev/null 2>&1 || \
docker run -d \
  --name ningipoints-postgres \
  --network ningipoints-network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=ningipoints \
  -p 5432:5432 \
  postgres:15

# Build da imagem da aplicação
docker build -t ningipoints-api .

# Sobe a aplicação FastAPI
docker run -d \
  --name ningipoints-api \
  --network ningipoints-network \
  -p 8080:8080 \
  ningipoints-api

# chmod +x run.sh
# ./run.sh