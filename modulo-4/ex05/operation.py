from enum import Enum
from utils import format_cents

class OperationType(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'

class Operation:
    '''classe simples em Python chamada Operation para representar uma
    operação com três parâmetros públicos'''
    def __init__(self, cents: int, op_type: str, description: str):
        '''Inicializacao da classe'''

        if cents <= 0:
            raise ValueError("Valor do 'cents' deve ser maior que zero.")

        try:
            self.op_type = OperationType(op_type.lower())
        except ValueError:
            raise ValueError("Tipo de operação deve ser 'credit' ou 'debit'.")
        
        self.cents = cents
        self.description = description

    def __repr__(self) -> str:
        '''Representacao do objeto'''
        try:
            return (
                f"Operation(cents={self.cents}, "
                f"op_type='{self.op_type}', "
                f"description='{self.description}')"
            )
        except Exception as e:
            raise e
    

    def __str__(self) -> str:
        '''print na tela'''
        try:
            sinal = '[+]' if self.op_type == OperationType.CREDIT else '[-]'

            return f"{sinal} {format_cents(self.cents)} ({self.description})"
        except Exception as e:
            raise e

# print(Operation(11_222_00, 'credit', 'ATM deposit'))
# print(Operation(41_256_08, 'debit', 'CEI saque'))

# >>> python3
# >>> from operation import Operation
# >>> t = Operation(11_222_00, 'credit', 'ATM deposit')
# >>> t
# Operation(cents=1122200, op_type='credit', description='ATM deposit')
# >>> t.cents
# >>> t.op_type
# >>> t.description
# >>> print(t)
# [+] R$ 11.222,00 (ATM deposit)
