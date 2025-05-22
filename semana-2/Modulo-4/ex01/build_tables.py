import os

# Simula credenciais (DynamoDB Local ignora isso, mas boto3 exige algo presente)
os.environ["AWS_ACCESS_KEY_ID"] = "fake"
os.environ["AWS_SECRET_ACCESS_KEY"] = "fake"

from models import Account

def create_tables() -> None:
    if not Account.exists():
        Account.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

if __name__ == "__main__":
    create_tables()



# ?> docker run -d \
# --name dynamodb-local \
# -p 8000:8000 \
# -v dynamodb-data:/home/dynamodblocal/data \
# amazon/dynamodb-local \
# -jar DynamoDBLocal.jar -sharedDb