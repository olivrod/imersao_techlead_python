from typing import Any

def inspect_arguments(*args: Any, **kwargs: Any) -> dict[int | str, Any] | None:
    '''Aceite qualquer número de argumentos posicionais e nomeados e retorna
    informações sobre quaisquer argumentos que sejam passados para ela'''

    # Se não houver argumentos
    if not args and not kwargs:
        print(None)
        return None
    
    result: dict[int | str, Any] = {}
    
    # Adiciona os argumentos posicionais ao dicionário
    for idx, value in enumerate(args):
        result[idx] = value
    
    # Adiciona os argumentos nomeados ao dicionário
    for key, value in kwargs.items():
        result[key] = value
    
    return result

# from arg_inspector import inspect_arguments
# >>> inspect_arguments(42, "hello", True, name="Alice", age=30, language="Python")
# {0: 42, 1: 'hello', 2: True, 'name': 'Alice', 'age': 30, 'language': 'Python'}
# >>> inspect_arguments()
# None
# >>> inspect_arguments(1, 2, 3)
# {0: 1, 1: 2, 2: 3}
# >>> inspect_arguments(city="Paris", country="France")
# {'city': 'Paris', 'country': 'France'}