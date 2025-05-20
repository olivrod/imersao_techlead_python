FROM python:3.10.12-bullseye
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# ?> docker build -t myserver .
# ?> docker run --rm -d -p 8000:8000 myserver
# <container hash>
# ?> curl localhost:8000
# {"message":"Bem-vindo à minha API!"}
# docker ps
# Para todos os dockers em execucao:
# docker stop $(docker ps -q)

# http POST http://localhost:8000/create name="João" age:=30 email="rxpbra@gmail.com" balance:=222.33
# http POST http://localhost:8000/create name:=2342 age:=30 email="rxpbra@gmail.com" balance:=222.33
# http POST http://localhost:8000/create name="João" age:=30 email="naoéemail" balance:=222.33
# http POST http://localhost:8000/create name="João" age="trinta" email="rxpbra@gmail.com" balance:=222.33
# http POST http://localhost:8000/create name="João" age:=30 email="rxpbra@gmail.com" balance="abc"
# http POST http://localhost:8000/create name:=123 age:=30 email="rxpbra@gmail.com" balance:=222.33
# http POST http://localhost:8000/create name:=123 age=trinta email=invalido balance=abc
# http POST http://localhost:8000/create name:=455 age:=-5 email=semarroba balance=abc

# http://127.0.0.1:8000/info
# http GET http://localhost:8000
# http POST http://localhost:8000/ nome="João" idade:=30
# http --form POST http://localhost:8000/ nome=João