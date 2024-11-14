class ReadOnlyDescriptor:
    """Deskryptor tylko dla odczytu"""
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        print('Odczytuje wartosc')
        return self._value
    
    def __set__(self, instance, value):
        print('Ustawiam wartosc')
        self._value = value

    def __delete__(self, instance):
        print('Usuwanie')
        del self._value
    
    
class MyClass:
    read_only = ReadOnlyDescriptor()

    def __init__(self, value):
        self.read_only = value

obj = MyClass(5)
print(obj.read_only)
print(ReadOnlyDescriptor.__doc__)