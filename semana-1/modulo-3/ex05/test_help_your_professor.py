import pytest
from help_your_professor import average

def test_lmedia_turma_3B():
    turma = {"marine": 18,"jean": 15,"coline": 8,"luc": 9}
    assert average(turma) == 12.5

def test_average_turma_3C():
    turma = {"quentin": 17, "julie": 15, "marc": 8, "stephanie": 13}
    assert average(turma) == 13.25

def test_average_turma_vazia():
    turma = {}
    assert average(turma) == 0.0

def test_media_nota_unica():
    turma = {"ana": 10}
    assert average(turma) == 10.0

def test_entrada_nao_dicionario():
    assert average("isso não é um dicionário") == 0.0

def test_valores_invalidos():
    turma = {"ana": "dez", "bia": 10}
    with pytest.raises(TypeError):  # soma de str + int causa erro
        average(turma)

def test_media_arredondamento_float():
    turma = {"a": 1, "b": 2}
    resultado = average(turma)
    assert resultado == 1.5
    assert isinstance(resultado, float)

# class_3B = {"marine": 18,"jean": 15,"coline": 8,"luc": 9}
# class_3C = {"quentin": 17,"julie": 15,"marc": 8,"stephanie": 13}
