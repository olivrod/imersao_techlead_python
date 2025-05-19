import sys
import json
from pathlib import Path
from pydantic import BaseModel, ValidationError, Field
from decimal import Decimal
from pydantic_core import ErrorDetails
from typing import Annotated

CUSTOM_MESSAGES = {
    'int_parsing': 'Deve ser inteiro',
    'string_type': 'Deve ser string',
    'decimal_parsing': 'Deve ser decimal',
}

def convert_errors(
    e: ValidationError, custom_messages: dict[str, str]
) -> list[ErrorDetails]:
    new_errors: list[ErrorDetails] = []
    for error in e.errors():
        custom_message = custom_messages.get(error['type'])
        if custom_message:
            ctx = error.get('ctx')
            error['msg'] = (
                custom_message.format(**ctx) if ctx else custom_message
            )
        new_errors.append(error)
    return new_errors

age: Annotated[int, lambda v: v > 0]

class Account(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    email: str
    balance: Decimal


def main(arquivo: Path) -> None:
    try:
        with open(arquivo, "r") as file:
            dados = json.load(file)
            # print(dados)
            Account(**dados)
            # print(conta)

    except ValidationError as e:
        errors = convert_errors(e, CUSTOM_MESSAGES)
        # print(errors)

        for erro in errors:
            loc = " -> ".join(str(p) for p in erro["loc"])
            msg = erro["msg"]
            print(f"{loc}: {msg}")

        # print("Erro de validacao de dados")
        # for erro in e.errors():
        #     loc = " -> ".join(str(p) for p in erro["loc"])
        #     msg = erro["msg"]
        #     tipo = erro["type"]
        #     print(f"- {loc}: {msg} (tipo: {tipo})")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Erro: o arquivo não contém um JSON válido.")
        sys.exit(1)
    except Exception as e:
        print(f"{e}")
        sys.exit(1)


if __name__ == "__main__":
    arquivo = Path(sys.argv[1])
    main(arquivo)
    

# python3 validate.py member.json