from arg_inspector import inspect_arguments

def test_inspect_arguments():
    # Teste com argumentos posicionais e nomeados
    result = inspect_arguments(42, "hello", True, name="Alice", age=30, language="Python")
    assert result == {0: 42, 1: 'hello', 2: True, 'name': 'Alice', 'age': 30, 'language': 'Python'}
    
    # Teste sem argumentos
    result = inspect_arguments()
    assert result is None
    
    # Teste com apenas argumentos posicionais
    result = inspect_arguments(1, 2, 3)
    assert result == {0: 1, 1: 2, 2: 3}
    
    # Teste com apenas argumentos nomeados
    result = inspect_arguments(city="Paris", country="France")
    assert result == {'city': 'Paris', 'country': 'France'}