from decimal import Decimal
from typing import Union
from calculator.operations import Operation  # Changed import
from calculator.calculation import Calculation

class Calculator:
    @staticmethod
    def add(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Operation._perform_operation(a, b, Operation.ADD)  # Updated to use Operation directly

    @staticmethod
    def subtract(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Operation._perform_operation(a, b, Operation.SUBTRACT)

    @staticmethod
    def multiply(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Operation._perform_operation(a, b, Operation.MULTIPLY)

    @staticmethod
    def divide(a: Union[int, float, str, Decimal], b: Union[int, float, str, Decimal]) -> Calculation:
        return Operation._perform_operation(a, b, Operation.DIVIDE)