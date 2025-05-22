from datetime import datetime
from fastapi.testclient import TestClient
from unittest.mock import patch
from api import app
from schemas import AccountRead, OperationRead, OperationType

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

def test_create_operation_success():
    payload = {
        "operation": "credit",
        "amount": 100
    }

    mock_operation = OperationRead(
        id=1,
        account_id=1,
        operation=OperationType.credit,
        amount=100,
        created_at=datetime.now()
    )

    with patch("api.get_account_id", return_value=AccountRead(id=1, name="João", email="joao@example.com")):
        with patch("api.add_operation", return_value=mock_operation):
            response = client.post("/accounts/1/operations", json=payload)
            assert response.status_code == 201
            assert response.json()["operation"] == "credit"
            assert response.json()["amount"] == 100

def test_create_operation_not_found():
    payload = {
        "operation": "debit",
        "amount": 50
    }

    with patch("api.get_account_id", return_value=None):
        response = client.post("/accounts/999/operations", json=payload)
        assert response.status_code == 404
        assert response.json()["detail"] == "Conta não encontrada"

def test_get_operations_success():
    mock_operations = [
        OperationRead(id=1, account_id=1, operation=OperationType.debit, amount=30, created_at=datetime.now()),
        OperationRead(id=2, account_id=1, operation=OperationType.credit, amount=50, created_at=datetime.now())
    ]

    with patch("api.get_operations_by_account_id", return_value=mock_operations):
        response = client.get("/accounts/1/operations")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]["operation"] == "debit"

def test_get_operations_no_content():
    with patch("api.get_operations_by_account_id", return_value=[]):
        response = client.get("/accounts/1/operations")
        assert response.status_code == 204