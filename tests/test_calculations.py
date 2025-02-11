"""Unit tests for the CalculationHistory class"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import CalculationHistory
from calculator.operations import Operation

@pytest.fixture(autouse=True)
def setup_teardown():
    """Fixture to clear calculation history before and after each test"""
    CalculationHistory.clear_history()
    yield
    CalculationHistory.clear_history()

def test_add_calculation():
    """Test adding a calculation to history"""
    calc = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    CalculationHistory.add_calculation(calc)
    assert len(CalculationHistory.get_history()) == 1
    assert CalculationHistory.get_last_calculation() == calc

def test_get_last_calculation_empty_history():
    """Test getting last calculation from empty history"""
    assert CalculationHistory.get_last_calculation() is None

def test_get_last_calculation():
    """Test getting last calculation from history"""
    calc1 = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    calc2 = Calculation(Decimal('20'), Decimal('5'), Operation.SUBTRACT, Decimal('15'))
    CalculationHistory.add_calculation(calc1)
    CalculationHistory.add_calculation(calc2)
    assert CalculationHistory.get_last_calculation() == calc2

def test_clear_history():
    """Test clearing calculation history"""
    calc = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    CalculationHistory.add_calculation(calc)
    CalculationHistory.clear_history()
    assert len(CalculationHistory.get_history()) == 0

def test_get_history():
    """Test getting calculation history"""
    calc1 = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    calc2 = Calculation(Decimal('20'), Decimal('5'), Operation.SUBTRACT, Decimal('15'))
    CalculationHistory.add_calculation(calc1)
    CalculationHistory.add_calculation(calc2)
    history = CalculationHistory.get_history()
    assert len(history) == 2
    assert history[0] == calc1
    assert history[1] == calc2

def test_history_is_copied():
    """Test that get_history returns a copy of the history"""
    calc = Calculation(Decimal('10'), Decimal('5'), Operation.ADD, Decimal('15'))
    CalculationHistory.add_calculation(calc)
    history = CalculationHistory.get_history()
    history.clear()
    assert len(CalculationHistory.get_history()) == 1
