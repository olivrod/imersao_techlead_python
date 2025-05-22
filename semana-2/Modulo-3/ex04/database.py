import os
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Accounts, Operations
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from schemas import AccountCreate, OperationCreate

load_dotenv()

DB_URL = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/{os.getenv('POSTGRES_DB')}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

def create_account(db: Session, account: AccountCreate) -> Accounts | None:
    if db.query(Accounts).filter(Accounts.id == account.id).first():
        return None
    db_account = Accounts(**account.model_dump())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

def get_all_accounts(db: Session) -> list[Accounts]:
    return db.query(Accounts).all()

def get_account_id(db: Session, account_id: int) -> Accounts | None:
    return db.query(Accounts).filter(Accounts.id == account_id).first()

def add_operation(db: Session, account_id: int, operation: OperationCreate) -> Operations:
    db_op = Operations(
        account_id=account_id,
        operation=operation.operation,
        amount=operation.amount
    )
    db.add(db_op)
    db.commit()
    db.refresh(db_op)
    return db_op

def get_operations_by_account_id(db: Session, account_id: int) -> List[Operations]:
    return db.query(Operations).filter(Operations.account_id == account_id).all()

