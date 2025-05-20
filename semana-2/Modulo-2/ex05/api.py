import datetime
import sys
from typing import Dict
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

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

# uvicorn api:app --reload
# http POST http://localhost:8000/ nome="João" idade:=30
# http --form POST http://localhost:8000/ nome=João
# http://127.0.0.1:8000/info
# http GET http://localhost:8000