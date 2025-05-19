from operation import Operation, OperationType
from utils import format_cents

class Account:
    def __init__(self, account_id: int, *cpfs: str):
        self.account_id = account_id
        self.cpfs = list(cpfs)
        self.__balance = 0
        self.__operations: list[Operation] = []

    def deposit(self, amount: int, description: str) -> None:
        if amount <= 0:
            raise ValueError("valor deve ser > 0")
        self.__balance += amount
        self.__operations.append(Operation(amount, OperationType.CREDIT.value, description))

    def withdraw(self, amount: int, description: str) -> None:
        if amount <= 0:
            raise ValueError("valor deve ser > 0")
        if amount > self.__balance:
            raise ValueError("saldo insuficiente")
        self.__balance -= amount
        self.__operations.append(Operation(amount, OperationType.DEBIT.value, description))

    def statement(self) -> None:
        for op in self.__operations:
            print(op)
        sinal = '[+]' if self.__balance >= 0 else '[-]'
        print(f"Balance: {sinal} {format_cents(self.__balance)}")

    def __str__(self) -> str:
        sinal = '[+]' if self.__balance >= 0 else '[-]'
        return f"Account: {self.account_id}\nBalance: {sinal} {format_cents(self.__balance)}"

    def __repr__(self) -> str:
        return f"Account({self.account_id}, ...)"
    

# >>> from account import Account
# >>> ac = Account(123, '123.456.789-01', '234.567.890.12')
# >>> ac
# Account(123, ...)
# >>> print(ac)
# Account: 123
# Balance: [+] R$ 0,00
# >>> ac.deposit(1122200, 'ATM deposit')
# >>> ac.statement()
# [+] R$ 11.222,00 (ATM deposit)
# Balance: [+] R$ 11.222,00