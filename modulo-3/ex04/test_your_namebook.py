import pytest
from your_namebook import list_of_names

def test_lista_simples():
    nomes = {"jean": "valjean", "grace": "hopper"}
    resultado = list_of_names(nomes)
    assert resultado == ["Jean Valjean", "Grace Hopper"]

def test_dicionario_vazio():
    nomes = {}
    resultado = list_of_names(nomes)
    assert resultado == []

def test_nomes_ja_maiusculos():
    nomes = {"JEAN": "VALJEAN", "grAce": "hOppEr"}
    resultado = list_of_names(nomes)
    assert resultado == ["Jean Valjean", "Grace Hopper"]

def test_valores_invalidos_erro():
    with pytest.raises(AttributeError):
        nomes = {"ana": None}
        list_of_names(nomes)

def test_argumento_invalido_tipo():
    with pytest.raises(AttributeError):
        list_of_names("isso não é um dicionário")