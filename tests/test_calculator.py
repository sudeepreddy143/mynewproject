"""
Unit tests for the Calculator module.
"""
# pylint: disable=unused-argument

from decimal import Decimal
import pytest
from calculator import Calculator, Operation, CalculationHistory


@pytest.fixture
def clear_history_fixture():
    """Clears calculation history before each test"""
    CalculationHistory.clear_history()
    yield
    CalculationHistory.clear_history()
@pytest.mark.parametrize(
    "num1, num2, operation, expected, expected_repr",
    [
        (
            Decimal('10'),
            Decimal('5'),
            Operation.ADD,
            Decimal('15'),
            "Calculation(a=Decimal('10'), b=Decimal('5'), operation=Operation.ADD, "
            "result=Decimal('15'))"
        ),
        (
            Decimal('-1'),
            Decimal('1'),
            Operation.ADD,
            Decimal('0'),
            "Calculation(a=Decimal('-1'), b=Decimal('1'), operation=Operation.ADD, "
            "result=Decimal('0'))"
        ),
        (
            Decimal('0'),
            Decimal('0'),
            Operation.ADD,
            Decimal('0'),
            "Calculation(a=Decimal('0'), b=Decimal('0'), operation=Operation.ADD, "
            "result=Decimal('0'))"
        ),
        (
            Decimal('2.5'),
            Decimal('3.5'),
            Operation.ADD,
            Decimal('6.0'),
            "Calculation(a=Decimal('2.5'), b=Decimal('3.5'), operation=Operation.ADD, "
            "result=Decimal('6.0'))"
        ),
    ],
)
def test_addition(num1, num2, operation, expected, expected_repr):
    """Test addition"""
    calc = Calculator.add(num1, num2)
    assert (calc.a, calc.b, calc.operation, calc.result) == (num1, num2, operation, expected)
    assert repr(calc) == expected_repr


@pytest.mark.parametrize(
    "num1, num2, operation, expected, expected_repr",
    [
        (
            Decimal('10'),
            Decimal('5'),
            Operation.SUBTRACT,
            Decimal('5'),
            "Calculation(a=Decimal('10'), b=Decimal('5'), operation=Operation.SUBTRACT, "
            "result=Decimal('5'))"
        ),
        (
            Decimal('-1'),
            Decimal('-1'),
            Operation.SUBTRACT,
            Decimal('0'),
            "Calculation(a=Decimal('-1'), b=Decimal('-1'), operation=Operation.SUBTRACT, "
            "result=Decimal('0'))"
        ),
        (
            Decimal('0'),
            Decimal('5'),
            Operation.SUBTRACT,
            Decimal('-5'),
            "Calculation(a=Decimal('0'), b=Decimal('5'), operation=Operation.SUBTRACT, "
            "result=Decimal('-5'))"
        ),
        (
            Decimal('3.5'),
            Decimal('2.0'),
            Operation.SUBTRACT,
            Decimal('1.5'),
            "Calculation(a=Decimal('3.5'), b=Decimal('2.0'), operation=Operation.SUBTRACT, "
            "result=Decimal('1.5'))"
        ),
    ],
)
def test_subtraction(num1, num2, operation, expected, expected_repr):
    """Test subtraction"""
    calc = Calculator.subtract(num1, num2)
    assert (calc.a, calc.b, calc.operation, calc.result) == (num1, num2, operation, expected)
    assert repr(calc) == expected_repr


@pytest.mark.parametrize(
    "num1, num2, operation, expected, expected_repr",
    [
        (
            Decimal('10'),
            Decimal('5'),
            Operation.MULTIPLY,
            Decimal('50'),
            "Calculation(a=Decimal('10'), b=Decimal('5'), operation=Operation.MULTIPLY, "
            "result=Decimal('50'))"
        ),
        (
            Decimal('-2'),
            Decimal('3'),
            Operation.MULTIPLY,
            Decimal('-6'),
            "Calculation(a=Decimal('-2'), b=Decimal('3'), operation=Operation.MULTIPLY, "
            "result=Decimal('-6'))"
        ),
        (
            Decimal('0'),
            Decimal('5'),
            Operation.MULTIPLY,
            Decimal('0'),
            "Calculation(a=Decimal('0'), b=Decimal('5'), operation=Operation.MULTIPLY, "
            "result=Decimal('0'))"
        ),
        (
            Decimal('2.5'),
            Decimal('2.5'),
            Operation.MULTIPLY,
            Decimal('6.25'),
            "Calculation(a=Decimal('2.5'), b=Decimal('2.5'), operation=Operation.MULTIPLY, "
            "result=Decimal('6.25'))"
        ),
    ],
)
def test_multiplication(num1, num2, operation, expected, expected_repr):
    """Test multiplication"""
    calc = Calculator.multiply(num1, num2)
    assert (calc.a, calc.b, calc.operation, calc.result) == (num1, num2, operation, expected)
    assert repr(calc) == expected_repr


@pytest.mark.parametrize(
    "num1, num2, operation, expected, expected_repr",
    [
        (
            Decimal('10'),
            Decimal('5'),
            Operation.DIVIDE,
            Decimal('2'),
            "Calculation(a=Decimal('10'), b=Decimal('5'), operation=Operation.DIVIDE, "
            "result=Decimal('2'))"
        ),
        (
            Decimal('-6'),
            Decimal('3'),
            Operation.DIVIDE,
            Decimal('-2'),
            "Calculation(a=Decimal('-6'), b=Decimal('3'), operation=Operation.DIVIDE, "
            "result=Decimal('-2'))"
        ),
        (
            Decimal('0'),
            Decimal('5'),
            Operation.DIVIDE,
            Decimal('0'),
            "Calculation(a=Decimal('0'), b=Decimal('5'), operation=Operation.DIVIDE, "
            "result=Decimal('0'))"
        ),
        (
            Decimal('5.0'),
            Decimal('2.0'),
            Operation.DIVIDE,
            Decimal('2.5'),
            "Calculation(a=Decimal('5.0'), b=Decimal('2.0'), operation=Operation.DIVIDE, "
            "result=Decimal('2.5'))"
        ),
    ],
)
def test_division(num1, num2, operation, expected, expected_repr):
    """Test division"""
    calc = Calculator.divide(num1, num2)
    assert (calc.a, calc.b, calc.operation, calc.result) == (num1, num2, operation, expected)
    assert repr(calc) == expected_repr


@pytest.mark.parametrize("num1, num2", [(Decimal('1'), Decimal('0'))])
def test_divide_by_zero(num1, num2):
    """Test division by zero raises an error"""
    with pytest.raises(ValueError, match="Division error: Division by zero is not allowed"):
        Calculator.divide(num1, num2)

def test_calculation_history(clear_history_fixture): # pylint: disable=redefined-outer-name
    """Test calculation history functionality"""
    calc1 = Calculator.add(Decimal(2), Decimal(3))
    calc2 = Calculator.multiply(Decimal(4), Decimal(5))
    calc3 = Calculator.subtract(Decimal(10), Decimal(3))

    history = CalculationHistory.get_history()
    assert len(history) == 3
    assert history[0] == calc1
    assert history[1] == calc2
    assert history[2] == calc3

    assert CalculationHistory.get_last_calculation() == calc3

    CalculationHistory.clear_history()
    assert len(CalculationHistory.get_history()) == 0
    assert CalculationHistory.get_last_calculation() is None

@pytest.mark.parametrize("num1, num2, operation", [
    ("invalid", 5, Operation.ADD),
    (5, "invalid", Operation.ADD),
    ("invalid", 5, Operation.SUBTRACT),
    (5, "invalid", Operation.SUBTRACT),
    ("invalid", 5, Operation.MULTIPLY),
    (5, "invalid", Operation.MULTIPLY),
    ("invalid", 5, Operation.DIVIDE),
    (5, "invalid", Operation.DIVIDE),
])

def test_invalid_inputs(num1, num2, operation):
    """Test operations with invalid inputs."""
    with pytest.raises(ValueError, match="Invalid number format"):
        if operation == Operation.ADD:
            Calculator.add(num1, num2)
        elif operation == Operation.SUBTRACT:
            Calculator.subtract(num1, num2)
        elif operation == Operation.MULTIPLY:
            Calculator.multiply(num1, num2)
        elif operation == Operation.DIVIDE:
            Calculator.divide(num1, num2)
