"""Module containing the Calculation class"""
from dataclasses import dataclass
from decimal import Decimal
from typing import TYPE_CHECKING, Any

@dataclass
class Calculation:
    """Class for storing calculation details"""
    a: Decimal
    b: Decimal
    operation: Any
    result: Decimal

    def __post_init__(self):
        """Validate operation type after initialization"""
        from calculator.operations import Operation
        if not isinstance(self.operation, Operation):
            raise ValueError("Invalid operation type")