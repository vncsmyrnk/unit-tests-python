import pytest
from calculator import Calculator;

calc = Calculator()

def test_sum():
    assert calc.add(1, 2) == 3

def test_sub():
    assert calc.sub(5, 3) == 2

def test_mul():
    assert calc.mul(4, 5) == 20

def test_div():
    assert calc.div(10, 2) == 5

def test_div_by_zero():
    assert calc.div(10, 0) == None
