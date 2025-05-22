FROM python:3.10.12-bullseye
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["bash", "run.sh"]


# Subir PostgreSQL com Docker
# export POSTGRES_PASSWORD=postgres

# docker run --name postgres \
#   -v postgres-data:/var/lib/postgresql/data \
#   -p 5432:5432 \
#   -e POSTGRES_DB=ningipoints \
#   -e POSTGRES_USER=postgres \
#   -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
#   -d postgres

# Criar tabelas:
# pip install sqlalchemy psycopg2-binary python-dotenv
# python3 build_tables.py

# docker ps -a
# Para o docker em execucao:
# docker stop ningipoints-postgres
# docker start ningipoints-postgres
# docker rm -f -v ningipoints-postgres

# psql -h localhost -U ningipoints-postgres -d ningipoints
# \dt
