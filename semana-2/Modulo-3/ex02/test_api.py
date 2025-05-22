from fastapi.testclient import TestClient
from unittest.mock import patch
from api import app
from schemas import AccountRead

client = TestClient(app)

def test_create_account_success():
    payload = {
        "id": 1,
        "name": "João da Silva",
        "email": "joao@example.com"
    }

    mock_account = AccountRead(id=1, name=payload["name"], email=payload["email"])

    with patch("api.create_account", return_value=mock_account):
        response = client.put("/accounts", json=payload)
        assert response.status_code == 201
        assert response.json()["name"] == "João da Silva"
        assert response.json()["email"] == "joao@example.com"

def test_create_account_conflict():
    payload = {
        "id": 1,
        "name": "Maria",
        "email": "maria@example.com"
    }

    with patch("api.create_account", return_value=None):
        response = client.put("/accounts", json=payload)
        assert response.status_code == 409
        assert response.json()["detail"] == "Conta já existe"
