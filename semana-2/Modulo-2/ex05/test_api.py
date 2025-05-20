from fastapi.testclient import TestClient
from api import app

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

def test_post_root_invalid_json():
    # envia texto em vez de JSON
    response = client.post("/", data="not json", headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert "error" in response.json()

def test_get_info():
    response = client.get("/info")
    assert response.status_code == 200
    data = response.json()
    assert "now" in data
    assert "version" in data
