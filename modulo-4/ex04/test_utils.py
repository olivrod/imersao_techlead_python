import pytest
from utils import format_cents

@pytest.mark.parametrize("entrada,saida_esperada", [
    (1122200, "R$ 11.222,00"), 
    (999, "R$ 9,99"), 
    (0, "R$ 0,00"), 
    (1, "R$ 0,01"), 
    (-1122200, "-R$ 11.222,00"), 
    (-999, "-R$ 9,99"), 
])
def test_format_cents_valores_validos(entrada, saida_esperada):
    assert format_cents(entrada) == saida_esperada


def test_format_cents_entrada_invalida():
    # Passa algo que não é inteiro
    resultado = format_cents("abc")
    assert resultado.startswith("Erro inesperado:")
