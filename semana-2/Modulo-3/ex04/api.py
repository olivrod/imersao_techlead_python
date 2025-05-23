from decimal import Decimal
from typing import List, Union
from fastapi import Depends, FastAPI, HTTPException, Response
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from schemas import AccountCreate, AccountRead, OperationCreate, OperationRead
from collections.abc import Generator
from models import Accounts
from database import (
    SessionLocal,
    create_account,
    get_all_accounts,
    get_account_id,
    add_operation,
    get_operations_by_account_id
)

app = FastAPI()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Account(BaseModel):
    name: str
    email: EmailStr
    balance: Decimal
    
@app.put("/accounts", response_model=AccountRead, status_code=201)
def put_account(account: AccountCreate, db: Session = Depends(get_db)) -> AccountRead:
    result = create_account(db, account)
    if not result:
        raise HTTPException(status_code=409, detail="Conta já existe")
    return result

@app.get("/accounts", response_model=list[AccountRead])
def list_accounts(db: Session = Depends(get_db)) -> List[Accounts]:
    accounts = get_all_accounts(db)
    if not accounts:
        raise HTTPException(status_code=204, detail=None)
    return accounts

@app.get("/accounts/{account_id}", response_model=AccountRead)
def read_account(account_id: int, db: Session = Depends(get_db)) -> Accounts:
    account = get_account_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return account

@app.post("/accounts/{account_id}/operations", response_model=OperationRead, status_code=201)
def post_operation(account_id: int, operation: OperationCreate, db: Session = Depends(get_db)) -> OperationRead:
    account = get_account_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return add_operation(db, account_id, operation)

@app.get("/accounts/{account_id}/operations", response_model=List[OperationRead])
def get_operations(account_id: int, db: Session = Depends(get_db)) -> Union[List[OperationRead], Response]:
    operations = get_operations_by_account_id(db, account_id)
    if not operations:
        return Response(status_code=204)
    return [OperationRead.model_validate(op) for op in operations]


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