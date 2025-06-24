import sys
import boto3
import csv
from decode import decode_and_upload

TABLE_NAME = "Usuarios"
BUCKET_NAME = "42sp-rde-oliv-bucket"  # Substitua SEU_LOGIN pelo seu login

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def load_csv(csv_path):
    print(f"Carregando dados de {csv_path}")
    csv.field_size_limit(sys.maxsize)
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            item = {"id": row["id"], "name": row["name"]}
            if "document" in row and row["document"].strip():
                image_key = decode_and_upload(row["document"], BUCKET_NAME)
                item["document_key"] = image_key
            table.put_item(Item=item)

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


# python3 dynamo_crud.py load users_with_documents.csv
# ?> python3 dynamo_crud.py retrieve u882
# Usuário encontrado: {'name': 'Zaphod Beeblebrox', 'id': 'u882', 'document_key': '882320-2939223-82823.jpg'}