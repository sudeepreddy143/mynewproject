import pytest
from calculator import Calculator

@pytest.mark.parametrize("num1, num2, method, expected", [
    (5, 3, Calculator.add, 8),
    (10, 4, Calculator.subtract, 6),
    (6, 7, Calculator.multiply, 42),
    (20, 5, Calculator.divide, 4)
])
def test_calculator_operations(num1, num2, method, expected):
    assert method(num1, num2) == expected

def test_calculator_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(10, 0)
