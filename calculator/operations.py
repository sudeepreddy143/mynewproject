from decimal import Decimal, InvalidOperation
from enum import Enum
from typing import Union
from calculator.calculation import Calculation
from calculator.calculations import CalculationHistory

class Operation(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'

    @staticmethod
    def convert_to_decimal(value: Union[int, float, str, Decimal]) -> Decimal:
        """Convert a value to Decimal."""
        if isinstance(value, Decimal):
            return value
        try:
            return Decimal(str(value))
        except InvalidOperation as e:
            raise ValueError(f"Invalid number format: {value}") from e

    @staticmethod
    def _perform_operation(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal], operation) -> Calculation:
        """Helper function to perform a calculation."""
        decimal_a = Operation.convert_to_decimal(a) 
        decimal_b = Operation.convert_to_decimal(b)
        
        if operation == Operation.ADD:
            result = decimal_a + decimal_b
        elif operation == Operation.SUBTRACT:
            result = decimal_a - decimal_b
        elif operation == Operation.MULTIPLY:
            result = decimal_a * decimal_b
        elif operation == Operation.DIVIDE:
            if decimal_b == Decimal('0'):
                raise ValueError("Division error: Division by zero is not allowed")
            result = decimal_a / decimal_b
        else:
            raise ValueError("Unsupported operation")
        
        calc = Calculation(decimal_a, decimal_b, operation, result)
        CalculationHistory.add_calculation(calc)
        return calc