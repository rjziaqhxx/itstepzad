class Operation:
    def __call__(self):
        raise NotImplemented
    
    def name(self):
        return self.__class__.__name__

class Addition(Operation):
    def __call__(self, x, y):
        return x + y

class Multiply(Operation):
    def __call__(self, x, y):
        return x * y

class Division(Operation):
    def __call__(self, x, y):
        if y == 0:
            raise ValueError('Cannot divide by zero')
        return x / y

class Substraction(Operation):
    def __call__(self, x, y):
        return x - y




class Calculator():
    def __init__(self, operations):
        self.operations = []

    def add_operation(self, operation):
        self.operations.append(operation)

    def calculate(self, x, y):
        for operation in self.operations:
            result = operation(x,y)
            print(f'Result of {operation.name} = {result}')


calc = Calculator(Operation)
calc.add_operation(Addition())
calc.add_operation(Multiply())
calc.add_operation(Division())
calc.add_operation(Substraction())
calc.calculate(10,5)