import enum
import os
from datetime import datetime
from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute,
    NumberAttribute,
    ListAttribute,
    MapAttribute,
    UTCDateTimeAttribute
)

# Configuração para rodar localmente
os.environ["AWS_ACCESS_KEY_ID"] = "fake"
os.environ["AWS_SECRET_ACCESS_KEY"] = "fake"

class OperationType(enum.Enum):
    debit = "debit"
    credit = "credit"

class Operation(MapAttribute):
    operation = UnicodeAttribute()
    amount = NumberAttribute()
    created_at = UTCDateTimeAttribute(default=str(datetime.now()))

    def as_dict(self):
        return {
            "operation": self.operation,
            "amount": float(self.amount),
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_input(cls, operation: str, amount: float):
        if operation not in OperationType._value2member_map_:
            raise ValueError(f"Operação inválida: {operation}")
        return cls(
            operation=operation,
            amount=amount,
            created_at=datetime.utcnow()
        )

class Account(Model):
    class Meta:
        table_name = "accounts"
        region = "us-east-1"
        host = os.getenv("DYNAMODB_URL", "http://localhost:8000")

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)
    balance = NumberAttribute(default=float("0.0"))
    operations = ListAttribute(of=Operation, default=list)
