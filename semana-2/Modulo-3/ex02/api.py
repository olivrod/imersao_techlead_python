from decimal import Decimal
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from database import SessionLocal, create_account
from schemas import AccountCreate, AccountRead
from collections.abc import Generator

app = FastAPI()

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Account(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr
    balance: Decimal
    
@app.put("/accounts", response_model=AccountRead, status_code=201)
def put_account(account: AccountCreate, db: Session = Depends(get_db)) -> AccountRead:
    result = create_account(db, account)
    if not result:
        raise HTTPException(status_code=409, detail="Conta já existe")
    return result

# uvicorn api:app --reload
# curl -X PUT http://localhost:8000/accounts -H "Content-Type: application/json" -d '{"id": 1, "name": "João da Silva", "email": "joao@example.com"}'

# pytest test_api.py