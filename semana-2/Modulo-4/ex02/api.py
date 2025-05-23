from fastapi import FastAPI, HTTPException, Response
from typing import List, Union
from schemas import AccountCreate, AccountRead, OperationCreate, OperationRead
from fastapi.encoders import jsonable_encoder
from database import (
    create_account,
    get_all_accounts,
    get_account_id,
    add_operation,
    get_operations_by_account_id,
    delete_account
)

app = FastAPI()

@app.put("/accounts", response_model=AccountRead, status_code=201)
def put_account(account: AccountCreate) -> AccountRead:
    result = create_account(account)
    if not result:
        raise HTTPException(status_code=409, detail="Conta já existe")
    return AccountRead(**result.attribute_values)

@app.get("/accounts", response_model=List[AccountRead])
def list_accounts() -> List[AccountRead]:
    accounts = get_all_accounts()
    if not accounts:
        return Response(status_code=204)

    return [
        AccountRead(
            id=int(account.id),
            name=account.name,
            email=account.email,
            balance=float(account.balance),
            operations=[
                OperationRead(
                    operation=op.operation,
                    amount=float(op.amount),
                    created_at=op.created_at.isoformat()
                ) for op in account.operations
            ]
        )
        for account in accounts
    ]

@app.get("/accounts/{account_id}", response_model=AccountRead)
def read_account(account_id: int) -> AccountRead:
    account = get_account_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    
    return AccountRead(
        id=int(account.id),
        name=account.name,
        email=account.email,
        balance=float(account.balance),
        operations=[
            OperationRead(
                operation=op.operation,
                amount=float(op.amount),
                created_at=op.created_at.isoformat()
            ) for op in account.operations
        ]
    )

@app.post("/accounts/{account_id}/operations", response_model=OperationRead, status_code=201)
def post_operation(account_id: int, operation: OperationCreate) -> OperationRead:
    op = add_operation(account_id, operation)
    if not op:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return OperationRead(**op)

@app.get("/accounts/{account_id}/operations", response_model=List[OperationRead])
def get_operations(account_id: int) -> Union[List[OperationRead], Response]:
    operations = get_operations_by_account_id(account_id)
    if not operations:
        return Response(status_code=204)
    return [OperationRead.model_validate(op) for op in operations]

@app.delete("/accounts/{account_id}", status_code=204)
def delete_account_endpoint(account_id: int) -> None:
    result = delete_account(account_id)
    if not result:
        raise HTTPException(status_code=404, detail="Conta não encontrada")


# uvicorn api:app --reload
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 1, "name": "João da Silva", "email": "joao@example.com"}'
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 2, "name": "Maria da Silva", "email": "maria@example.com"}'
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 3, "name": "Sergio da Silva", "email": "sergio@example.com"}'
# curl -X GET http://localhost:8000/accounts -H "Content-Type: application/json"
# curl -X GET http://localhost:8000/accounts/3 -H "Content-Type: application/json"

# curl -X POST http://localhost:8000/accounts/1/operations -H "Content-Type: application/json" -d '{"operation": "credit", "amount": 100}'
# curl http://localhost:8000/accounts/1/operations

# pytest test_api.py

# {"id": 1, "name": "Joao da Silva", "email": "joao@example.com"}
# {"id": 2, "name": "Maria da Silva", "email": "maria@example.com"}
# {"id": 3, "name": "Sergio da Silva", "email": "sergio@example.com"}