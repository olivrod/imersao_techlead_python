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

def test_list_accounts_found():
    mock_accounts = [
        AccountRead(id=1, name="João da Silva", email="joao@example.com"),
    ]

    with patch("api.get_all_accounts", return_value=mock_accounts):
        response = client.get("/accounts")
        assert response.status_code == 200
        assert response.json() == [account.model_dump() for account in mock_accounts]

def test_list_accounts_empty():
    with patch("api.get_all_accounts", return_value=[]):
        response = client.get("/accounts")
        assert response.status_code == 204

def test_read_account_success():
    mock_account = AccountRead(id=1, name="João da Silva", email="joao@example.com")

    with patch("api.get_account_id", return_value=mock_account):
        response = client.get("/accounts/1")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert data["name"] == "João da Silva"

def test_read_account_not_found():
    with patch("api.get_account_id", return_value=None):
        response = client.get("/accounts/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Conta não encontrada"