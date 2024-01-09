# tests/test_calculator.py
from my_package.calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.subtract(5, 2)
    assert result == 3
