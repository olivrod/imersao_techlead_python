import pytest
from account import Account, InsufficientBalance
from operation import OperationType


def test_account_criacao():
    ac = Account(123, '123.456.789-01', '234.567.890.12')
    assert ac.account_id == 123
    assert isinstance(ac.cpfs, list)
    assert len(ac.cpfs) == 2
    assert str(ac).startswith("Account: 123")
    assert repr(ac) == "Account(123, ...)"

def test_deposito_valido():
    ac = Account(1, '123.456.789-00')
    ac.deposit(10000, 'Depósito')
    assert ac._Account__balance == 10000
    assert len(ac._Account__operations) == 1
    op = ac._Account__operations[0]
    assert op.cents == 10000
    assert op.op_type == OperationType.CREDIT
    assert op.description == 'Depósito'

def test_deposito_invalido():
    ac = Account(2, '000.000.000-00')
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        ac.deposit(0, 'Depósito')

def test_saque_valido():
    ac = Account(3, '111.111.111-11')
    ac.deposit(50000, 'Depósito')
    ac.withdraw(30000, 'Saque')
    assert ac._Account__balance == 20000
    assert len(ac._Account__operations) == 2
    saque = ac._Account__operations[1]
    assert saque.cents == 30000
    assert saque.op_type == OperationType.DEBIT
    assert saque.description == 'Saque'

def test_saque_valor_invalido():
    ac = Account(4, '222.222.222-22')
    ac.deposit(10000, 'Depósito')
    with pytest.raises(ValueError, match="valor deve ser > 0"):
        ac.withdraw(0, 'Erro')

def test_statement(capsys):
    ac = Account(6, '444.444.444-44')
    ac.deposit(1122200, 'ATM deposit')
    ac.withdraw(2200, 'Compra')
    ac.statement()
    captured = capsys.readouterr().out
    assert '[+] R$ 11.222,00 (ATM deposit)' in captured
    assert '[-] R$ 22,00 (Compra)' in captured
    assert 'Balance: [+] R$ 11.200,00' in captured

def test_withdraw_insufficient_balance():
    acc = Account(100, "123.456.789-00")
    acc.deposit(10000, "initial deposit")

    with pytest.raises(InsufficientBalance):
        acc.withdraw(20000, "big withdrawal")
