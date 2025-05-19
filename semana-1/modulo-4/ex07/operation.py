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


