from calculator.operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(num1, num2):
        calculation = calculation(num1, num2, add)
        return calculation.get_result()

    @staticmethod
    def subtract(num1, num2):
        calculation = calculation(num1, num2, subtract)
        return calculation.get_result()

    @staticmethod
    def multiply(num1, num2):
        calculation = calculation(num1, num2, multiply)
        return calculation.get_result()

    @staticmethod
    def divide(num1, num2):
        calculation = calculation(num1, num2, divide)
        return calculation.get_result()
