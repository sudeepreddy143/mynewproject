'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(4,3) == 7

def test_subtraction():
    '''Test that addition function works '''    
    assert subtract(9,3) == 6

def test_multiplication():
    '''Test that multiply works'''
    assert multiply(3,9) == 27

def test_division():
    '''Test division'''
    assert divide(10,2) == 5
    