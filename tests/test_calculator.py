"""Unit tests for the Calculator class"""
from calculator import Calculator

def test_addition():
    """Test that addition function works"""
    calc = Calculator.add(2, 2)
    assert calc.result == 4

def test_subtraction():
    """Test that subtraction function works"""
    calc = Calculator.subtract(2, 2)
    assert calc.result == 0

def test_divide():
    """Test that division function works"""
    calc = Calculator.divide(2, 2)
    assert calc.result == 1

def test_multiply():
    """Test that multiply function works"""
    calc = Calculator.multiply(2, 2)
    assert calc.result == 4
