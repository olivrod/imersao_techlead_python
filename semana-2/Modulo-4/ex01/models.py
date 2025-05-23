import enum
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    ListAttribute,
    MapAttribute,
    UTCDateTimeAttribute
)
from datetime import datetime
import os

# Configuração mínima necessária para rodar com DynamoDB Local
os.environ["AWS_ACCESS_KEY_ID"] = "fake"
os.environ["AWS_SECRET_ACCESS_KEY"] = "fake"

class OperationType(enum.Enum):
    debit = "debit"
    credit = "credit"
    
class Operation(MapAttribute):
    operation = UnicodeAttribute()  # "debit" ou "credit"
    amount = NumberAttribute()      # Valor da operação
    created_at = UTCDateTimeAttribute(default=str(datetime.now())) 
    
    def __init__(self, **attributes):
        if "operation" in attributes:
            op = attributes["operation"]
            if isinstance(op, OperationType):
                attributes["operation"] = op.value
            elif op not in OperationType._value2member_map_:
                raise ValueError(f"Operação inválida: {op}")
        super().__init__(**attributes)

class Account(Model):
    class Meta:
        table_name = "accounts"
        region = "us-east-1"
        host = os.getenv("DYNAMODB_URL", "http://localhost:8000")  # URL do DynamoDB Local

    id = NumberAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    balance = NumberAttribute(default=float("0.0"))
    operations = ListAttribute(of=Operation, default=list)
