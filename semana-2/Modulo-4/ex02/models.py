from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, ListAttribute, MapAttribute
from datetime import datetime

class Operation(MapAttribute): # type: ignore
    operation_type = UnicodeAttribute()
    amount = NumberAttribute()
    created_at = UnicodeAttribute(default=lambda: datetime.now().isoformat())

class Account(Model):
    class Meta:
        table_name = "accounts"
        region = "us-east-1"
        host = "http://localhost:8000"  # ou use o IP do container se necessário

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    email = UnicodeAttribute()
    operations = ListAttribute(of=Operation)
