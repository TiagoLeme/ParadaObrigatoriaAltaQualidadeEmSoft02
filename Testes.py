# tests/test_adicao.py
import pytest
from Calculadora import adicao

def test_adicao_inteiros():
    assert adicao(2, 3) == 5

def test_adicao_negativos():
    assert adicao(-1, 1) == 0

def test_adicao_float():
    assert adicao(0.5, 0.25) == pytest.approx(0.75)


# tests/test_divisao.py
import pytest
from Calculadora import divisao

def test_divisao_normais():
    assert divisao(6, 3) == 2

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        divisao(10, 0)


# tests/test_input_utils.py
from Calculadora import input_float, input_int

def test_input_float(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3.14")
    assert input_float("prompt") == 3.14

def test_input_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "7")
    assert input_int("prompt") == 7
