import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
