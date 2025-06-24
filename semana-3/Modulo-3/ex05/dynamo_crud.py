import sys
import boto3
import csv

TABLE_NAME = "Usuarios"
ENDPOINT_URL = "http://localhost:4566"
REGION = "us-east-1"

dynamodb = boto3.resource(
    "dynamodb",
    endpoint_url=ENDPOINT_URL,
    region_name=REGION,
    aws_access_key_id="test",
    aws_secret_access_key="test"
)
table = dynamodb.Table(TABLE_NAME)

def load_csv(csv_path):
    print(f"Carregando dados de {csv_path}")
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            table.put_item(Item={"id": row["id"], "name": row["name"]})

def retrieve_user(user_id):
    response = table.get_item(Key={"id": user_id})
    item = response.get("Item")
    if item:
        print(f"Usuário encontrado: {item}")
    else:
        print(f"Usuário {user_id} não encontrado.")

def delete_user(user_id):
    table.delete_item(Key={"id": user_id})
    print(f"Usuário {user_id} removido.")

def update_user(user_id, new_name):
    response = table.update_item(
        Key={"id": user_id},
        UpdateExpression="set #n = :name",
        ExpressionAttributeNames={"#n": "name"},
        ExpressionAttributeValues={":name": new_name},
        ReturnValues="UPDATED_NEW"
    )
    print(f"Usuário {user_id} atualizado para nome = '{new_name}'")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Validar os parametros!")
        sys.exit(1)

    command = sys.argv[1]

    if command == "load":
        load_csv(sys.argv[2])
    elif command == "retrieve":
        retrieve_user(sys.argv[2])
    elif command == "delete":
        delete_user(sys.argv[2])
    elif command == "update":
        if len(sys.argv) < 4:
            print("Uso: python3 dynamo_crud.py update <user_id> \"Novo Nome\"")
            sys.exit(1)
        update_user(sys.argv[2], sys.argv[3])
    else:
        print("Comando desconhecido.")


# python3 dynamo_crud.py load ./users.csv
# python3 dynamo_crud.py retrieve u304
# python3 dynamo_crud.py update u304 "Novo Nome"
# python3 dynamo_crud.py delete u304