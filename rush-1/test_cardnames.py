import pytest
from cardnames import *

tests_data = [("Maria Beatriz Oliveira", "Maria Beatriz Oliveira"),
              ("Joao Beatriz Oliveira Junior", "Joao Beatriz Oliveira Jr"), 
              ("Carlos Antonio Oliveira Neto", "Carlos Antonio Oliveira"),
              ("Maria Souza de Oliveira II", "Maria Souza de Oliveira II")]

@pytest.mark.parametrize("test_input, resultado", [("Maria Souza de Oliveira II", True),
                                                   ("Maria Souza de Oliveira Dias", False)])
def test_fit_tamanho(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit_tamanho(given)
    assert result == expected

@pytest.mark.parametrize("test_input, resultado", [("Maria da Souza de Oliveira II", "Maria Souza Oliveira II"),
                                                   ("Maria Vitor Souza de Oliveira Junior dos Anjos da Silva", "Maria Vitor Souza Oliveira Junior Anjos Silva"),
                                                   ("Maria Vitor Souza de Oliveira Junior e Anjos da Silva", "Maria Vitor Souza Oliveira Junior Anjos Silva")])
def test_fit_preposicao(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit_preposicao(given)
    assert result == expected

@pytest.mark.parametrize("test_input, resultado", [("Maria da Souza de Oliveira II", "M da Souza de Oliveira II"),
                                                   ("Mariana Ximenes", "Mariana Ximenes")])
def test_fit_maria(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit_maria(given)
    assert result == expected

@pytest.mark.parametrize("test_input, resultado", [("João Vitor Souza de Oliveira Junior", "João Vitor Souza de Oliveira Jr"),
                                                   ("Junior Vitor dos Santos", "Junior Vitor dos Santos")])
def test_fit_junior(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit_junior(given)
    assert result == expected

@pytest.mark.parametrize("test_input, resultado", [("João Victor Souza Oliveira", "João V Souza Oliveira"),
                                                   ("João Vitor Souza Oliveira Junior", "João Vitor Souza O Junior")])
def test_fit_nomes_intermediarios(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit_nomes_intermediarios(given)
    assert result == expected

@pytest.mark.parametrize("test_input, resultado", [("Maria João Vitor dos Souza de Oliveira Junior", "M João Vitor Souza O Jr")])
def test_fit(test_input, resultado):
    given = test_input
    expected = resultado
    result = fit(given)
    assert result == expected
