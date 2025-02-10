class calculation:
    def __init__(self, num1, num2, func):
        self.num1 = num1
        self.num2 = num2
        self.func = func

    def compute(self):
        return self.func(self.num1, self.num2)
