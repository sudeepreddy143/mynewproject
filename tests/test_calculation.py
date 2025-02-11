"""Unit tests for the Calculation class"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import Operation

def test_calculation_creation():
    """Test creating a valid Calculation object"""
    calc = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    assert calc.a == Decimal('10')
    assert calc.b == Decimal('5')
    assert calc.operation == Operation.ADD
    assert calc.result == Decimal('15')

def test_calculation_invalid_operation():
    """Test creating a Calculation with invalid operation type"""
    with pytest.raises(ValueError, match="Invalid operation type"):
        Calculation(Decimal('10'), Decimal('5'), '+', Decimal('15'))

def test_calculation_decimal_values():
    """Test Calculation handles decimal values correctly"""
    calc = Calculation(
        Decimal('10.5'),
        Decimal('5.5'),
        Operation.ADD,
        Decimal('16.0')
    )
    assert calc.a == Decimal('10.5')
    assert calc.b == Decimal('5.5')
    assert calc.result == Decimal('16.0')

def test_calculation_equality():
    """Test Calculation equality comparison"""
    calc1 = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    calc2 = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    calc3 = Calculation(Decimal('10'), Decimal('5'), Operation.SUBTRACT, Decimal('5'))
    assert calc1 == calc2
    assert calc1 != calc3

def test_calculation_string_representation():
    """Test Calculation string representation"""
    calc = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    str_repr = str(calc)
    assert '10' in str_repr
    assert '5' in str_repr
    assert 'ADD' in str_repr
    assert '15' in str_repr
