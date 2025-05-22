import datetime
import sys
from typing import Dict
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError, Field, EmailStr
from decimal import Decimal
from pydantic_core import ErrorDetails

app = FastAPI()

CUSTOM_MESSAGES = {
    'int_parsing': 'Deve ser inteiro',
    'string_type': 'Deve ser string',
    'decimal_parsing': 'Deve ser decimal',
    'email_parsing': 'Deve ser um email válido',
    'greater_than': 'Deve ser maior que {gt}',
}

class Account(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: EmailStr
    balance: Decimal

def convert_errors(
    e: ValidationError, custom_messages: dict[str, str]
) -> list[ErrorDetails]:
    new_errors: list[ErrorDetails] = []
    for error in e.errors():
        field = error["loc"][0]
        error_type = error["type"]

        if field == "email":
            error["msg"] = custom_messages.get("email_parsing", error["msg"])
        else:
            custom_msg = custom_messages.get(error_type)
            if custom_msg:
                ctx = error.get("ctx")
                error["msg"] = (
                    custom_msg.format(**ctx) if ctx else custom_msg
                )

        new_errors.append(error)
    return new_errors


@app.post("/create")
async def post_create(request: Request) -> JSONResponse:
    dados = await request.json()
    try:
        Account(**dados)
        return JSONResponse(status_code=201, content="Dados criados")
    except ValidationError as e:
        errors = convert_errors(e, CUSTOM_MESSAGES)
        error_dict = {}

        for erro in errors:
            loc = " -> ".join(str(p) for p in erro["loc"])
            msg = erro["msg"]
            error_dict[loc] = msg
            
        return JSONResponse(status_code=422, content={"errors": error_dict})
        

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Bem-vindo à minha API!"}

@app.post("/")
async def post_root(request: Request) -> JSONResponse:
    try:
        data = await request.json()
        return JSONResponse(status_code=201, content={"message": "Dados recebidos com sucesso", "data": data})
    except Exception:
        return JSONResponse(status_code=400, content={"error": "JSON inválido ou ausente"})
 
@app.get("/info")
async def get_info() -> Dict[str, str]:
    return {
        "now": str(datetime.datetime.now()),
        "version": sys.version
    }

