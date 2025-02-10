'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(4,3) == 7

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(9,3) == 6

def test_multiply():
    '''Test that addition function works '''    
    assert Calculator.multiply(3,9) == 27

def test_divide():
    '''Test that addition function works '''    
    assert Calculator.divide(10,2) == 5