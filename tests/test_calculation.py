import pytest
from calculator.calculation import calculation
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("num1, num2, func, expected", [
    (5, 3, add, 8),
    (10, 4, subtract, 6),
    (6, 7, multiply, 42),
    (20, 5, divide, 4)
])
def test_calculation(num1, num2, func, expected):
    calc = calculation(num1, num2, func)
    assert calc.compute() == expected

def test_calculation_divide_by_zero():
    calc = calculation(10, 0, divide)
    with pytest.raises(ZeroDivisionError):
        calc.compute()
