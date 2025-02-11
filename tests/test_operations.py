"""Unit tests for the Operation class"""
from decimal import Decimal
import pytest
from calculator.operations import Operation
from calculator.calculation import Calculation

def test_operation_enum_values():
    """Test that Operation enum has correct values"""
    assert Operation.ADD.value == '+'
    assert Operation.SUBTRACT.value == '-'
    assert Operation.MULTIPLY.value == '*'
    assert Operation.DIVIDE.value == '/'

def test_convert_to_decimal_valid_inputs():
    """Test convert_to_decimal with various valid inputs"""
    assert Operation.convert_to_decimal(10) == Decimal('10')
    assert Operation.convert_to_decimal(10.5) == Decimal('10.5')
    assert Operation.convert_to_decimal('10.5') == Decimal('10.5')
    assert Operation.convert_to_decimal(Decimal('10.5')) == Decimal('10.5')

def test_convert_to_decimal_invalid_inputs():
    """Test convert_to_decimal with invalid inputs"""
    with pytest.raises(ValueError):
        Operation.convert_to_decimal('abc')
    with pytest.raises(ValueError):
        Operation.convert_to_decimal('12.34.56')

def test_perform_operation_addition():
    """Test _perform_operation with addition"""
    result = Operation._perform_operation(5, 3, Operation.ADD)
    assert isinstance(result, Calculation)
    assert result.result == Decimal('8')
    assert result.operation == Operation.ADD

def test_perform_operation_subtraction():
    """Test _perform_operation with subtraction"""
    result = Operation._perform_operation(5, 3, Operation.SUBTRACT)
    assert result.result == Decimal('2')
    assert result.operation == Operation.SUBTRACT

def test_perform_operation_multiplication():
    """Test _perform_operation with multiplication"""
    result = Operation._perform_operation(5, 3, Operation.MULTIPLY)
    assert result.result == Decimal('15')
    assert result.operation == Operation.MULTIPLY

def test_perform_operation_division():
    """Test _perform_operation with division"""
    result = Operation._perform_operation(6, 2, Operation.DIVIDE)
    assert result.result == Decimal('3')
    assert result.operation == Operation.DIVIDE

def test_perform_operation_division_by_zero():
    """Test _perform_operation with division by zero"""
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        Operation._perform_operation(5, 0, Operation.DIVIDE)

def test_perform_operation_invalid_operation():
    """Test _perform_operation with invalid operation"""
    class FakeOperation:
        """Fake operation class for testing"""
    with pytest.raises(ValueError, match="Unsupported operation"):
        Operation._perform_operation(5, 3, FakeOperation())
