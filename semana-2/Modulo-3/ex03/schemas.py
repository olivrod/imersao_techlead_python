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
