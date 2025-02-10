from decimal import Decimal, InvalidOperation
from typing import Union
from calculator.calculation import Calculation, CalculationHistory, Operation
   
class Calculator:
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
    def _perform_operation(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal], operation: Operation) -> Calculation:
        """Helper function to perform a calculation."""
        decimal_a = Calculator.convert_to_decimal(a)
        decimal_b = Calculator.convert_to_decimal(b)
        
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

    @staticmethod
    def add(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Calculator._perform_operation(a, b, Operation.ADD)

    @staticmethod
    def subtract(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Calculator._perform_operation(a, b, Operation.SUBTRACT)

    @staticmethod
    def multiply(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Calculator._perform_operation(a, b, Operation.MULTIPLY)

    @staticmethod
    def divide(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Calculator._perform_operation(a, b, Operation.DIVIDE)
