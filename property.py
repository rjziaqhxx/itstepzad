property(fget=None, fset=None, fdel=None, doc=None)

class Example():
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return f'To jest wartosc {self._value}'
    
    def __str__(self):
        return f'Nasz objekt {self._value}'
    
    def set_value(self, value):
        if value >= 0:
            self._value = value
        else:
            raise ValueError('Value must be non-negative.')
        
    value = property(get_value, set_value)

instance = Example(10)

instance.value = 5
print(instance.value)