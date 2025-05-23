from decimal import Decimal
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from database import SessionLocal, create_account, get_account_id, get_all_accounts
from schemas import AccountCreate, AccountRead
from collections.abc import Generator
from models import Accounts

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


# uvicorn api:app --reload
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 1, "name": "João da Silva", "email": "joao@example.com"}'
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 2, "name": "Maria da Silva", "email": "maria@example.com"}'
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 3, "name": "Sergio da Silva", "email": "sergio@example.com"}'
# curl -X GET http://localhost:8000/accounts -H "Content-Type: application/json"
# curl -X GET http://localhost:8000/accounts/3 -H "Content-Type: application/json"

# pytest test_api.py

# {"id": 1, "name": "Joao da Silva", "email": "joao@example.com"}
# {"id": 2, "name": "Maria da Silva", "email": "maria@example.com"}
# {"id": 3, "name": "Sergio da Silva", "email": "sergio@example.com"}