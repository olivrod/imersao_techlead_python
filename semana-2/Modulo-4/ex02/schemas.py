from pydantic import BaseModel, EmailStr, Field
from typing import Literal, List
from decimal import Decimal
from datetime import datetime


class AccountCreate(BaseModel):
    id: int
    name: str
    email: EmailStr


class OperationCreate(BaseModel):
    operation: Literal["credit", "debit"]
    amount: Decimal


class OperationRead(BaseModel):
    operation: Literal["credit", "debit"]
    amount: Decimal
    created_at: str  # ISO format string
    # created_at: datetime # agora um datetime real


class AccountRead(BaseModel):
    id: int
    name: str
    email: EmailStr
    balance: float
    operations: List[OperationRead] = Field(default_factory=list)
