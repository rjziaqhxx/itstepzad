class MyClass:
    def __init__(self, value, value2, items):
        self.value = value 
        self.value2 = value2
        self.items = items

    def __str__(self):
        return f'To jest nasz objekt, a jego wartosc {self.value}'
    
    def __eq__(self, other):
        return self.value2 == other.value2
    
    def __ne__(self, other):
        return self.value != other.value
    
    def __lt__(self, other):
        if isinstance(other, MyClass):
            return self.value < other.value
        return NotImplemented
    
    def __le__(self, other):
        if isinstance(other, MyClass):
            return self.value <= other.value
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, MyClass):
            return self.value > other.value
        return NotImplemented
    
    def __ge__(self, other):
        if isinstance(other, MyClass):
            return self.value >= other.value
        return NotImplemented

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    


obj = MyClass(10, 5,[])

ojb2 = MyClass(10, 3,[])


obj3 = MyClass(10,8, [1,23,4,5,3])
print(obj3[0])
obj3[0] = 99
