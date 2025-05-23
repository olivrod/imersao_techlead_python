from typing import List, Optional
from decimal import Decimal
from pynamodb.exceptions import DoesNotExist

from models import Account, Operation
from schemas import AccountCreate, OperationCreate

def as_dict(self):
    return {
        "operation": self.operation,
        "amount": float(self.amount),  # <-- conversão aqui
        "created_at": self.created_at.isoformat(),
    }


def create_account(account: AccountCreate) -> Optional[Account]:
    # Verifica se já existe conta com o mesmo ID (hash key)
    try:
        existing = Account.get(str(account.id))
        return None  # já existe
    except DoesNotExist:
        pass

    new_account = Account(
        id=str(account.id),
        email=account.email,
        name=account.name,
        balance=float(0.0),  # em vez de Decimal("0.0")
        operations=[]
    )
    new_account.save()
    return new_account

def get_all_accounts() -> List[Account]:
    return list(Account.scan())

def get_account_id(account_id: int) -> Optional[Account]:
    try:
        return Account.get(str(account_id))
    except DoesNotExist:
        return None

def add_operation(account_id: int, operation: OperationCreate) -> Optional[dict]:
    account = get_account_id(account_id)
    if not account:
        return None

    new_op = Operation(
        operation=operation.operation,
        amount=float(operation.amount)  # CONVERTE Decimal para float
    )

    if operation.operation == "credit":
        account.balance += Decimal(str(operation.amount))
    else:
        account.balance -= Decimal(str(operation.amount))

    account.operations.append(new_op)
    account.save()

    return new_op.as_dict()

def get_operations_by_account_id(account_id: int) -> List[dict]:
    account = get_account_id(account_id)
    if not account or not account.operations:
        return []
    return [op.as_dict() for op in account.operations]

def delete_account(account_id: int) -> bool:
    account = get_account_id(account_id)
    if not account:
        return False
    account.delete()
    return True
