from transform import valida_par, quadrado

def test_valida_par_true():
    assert valida_par(2) is True
    assert valida_par(0) is True
    assert valida_par(100) is True

def test_valida_par_false():
    assert valida_par(1) is False
    assert valida_par(7) is False
    assert valida_par(-3) is False

def test_quadrado():
    assert quadrado(2) == 4
    assert quadrado(-3) == 9
    assert quadrado(0) == 0