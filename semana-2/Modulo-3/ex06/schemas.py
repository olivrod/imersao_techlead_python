from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, ConfigDict

class AccountCreate(BaseModel):
    id: int
    name: str
    email: EmailStr

class AccountRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str

class OperationType(str, Enum):
    debit = "debit"
    credit = "credit"

class OperationCreate(BaseModel):
    operation: OperationType
    amount: int

class OperationRead(OperationCreate):
    id: int
    account_id: int
    created_at: datetime

    class Config:
        from_attributes = True