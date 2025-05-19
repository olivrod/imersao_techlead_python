import pytest
from validate import Account
from pydantic import BaseModel, ValidationError, conint

def test_account():
    
    given = {
        "name": "Clara Melo",
        "age": 43,
        "email": "claramelo1982@42sp.org.br",
        "balance": 1000.00
    }
    expected = Account
    assert isinstance(Account(**given), expected)

def test_account_erro():
    
    with pytest.raises(ValidationError):
        given = {
            "name": "Clara Melo",
            "age": "erro na idade",
            "email": "claramelo1982@42sp.org.br",
            "balance": 1000.00
        }

        Account(**given)
