from fastapi.testclient import TestClient
from api import app  # Certifique-se de que o nome do arquivo onde está o FastAPI é "api.py"

client = TestClient(app)

def test_root_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à minha API!"}

def test_post_root_valid_json():
    payload = {"foo": "bar"}
    response = client.post("/", json=payload)
    assert response.status_code == 201
    assert response.json()["message"] == "Dados recebidos com sucesso"
    assert response.json()["data"] == payload

def test_get_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "now" in data
    assert "version" in data

def test_post_create_valid_data():
    payload = {
        "name": "Maria",
        "age": 25,
        "email": "maria@email.com",
        "balance": "500.00"
    }
    response = client.post("/create", json=payload)
    assert response.status_code == 201
    assert response.json() == "Dados criados"

def test_post_create_invalid_data():
    payload = {
        "name": 123,                # inválido: não é string
        "age": -10,                 # inválido: menor que 0
        "email": "invalido",        # inválido: não é email
        "balance": "abc"            # inválido: não é decimal
    }
    response = client.post("/create", json=payload)
    assert response.status_code == 422

    data = response.json()
    assert "errors" in data
    errors = data["errors"]

    assert "name" in errors
    assert "age" in errors
    assert "email" in errors
    assert "balance" in errors
