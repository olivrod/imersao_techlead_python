import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Accounts
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from schemas import AccountCreate

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
