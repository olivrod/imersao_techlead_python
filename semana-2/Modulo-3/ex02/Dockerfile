FROM python:3.10.12-bullseye
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# Subir PostgreSQL com Docker
# export POSTGRES_PASSWORD=asd123

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
# docker stop postgres
# docker start postgres
# docker rm -f -v postgres

# psql -h localhost -U postgres -d ningipoints
# \dt
