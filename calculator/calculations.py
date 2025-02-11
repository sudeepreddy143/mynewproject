from typing import List, Union
from calculator.calculation import Calculation

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