class Fibonacci:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __call__(self):
        self.result = self.value1 + self.value2
        self.value1 = self.value2
        self.value2 = self.result
        return self.value1, self.value2
    
liczb = Fibonacci(0,1)
for i in range(10):
    print(liczb())
     