from enum import Enum
from typing import List, Union
from dataclasses import dataclass
from decimal import Decimal

class Operation(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    
@dataclass
class Calculation:
    a: Decimal
    b: Decimal
    operation: Operation
    result: Decimal

    def __str__(self) -> str:
        return f"{self.a} {self.operation.value} {self.b} = {self.result}"

    def __repr__(self) -> str:
        return f"Calculation(a=Decimal('{self.a}'), b=Decimal('{self.b}'), operation=Operation.{self.operation.name}, result=Decimal('{self.result}'))"

class CalculationHistory:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Union[Calculation, None]:
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history.copy()