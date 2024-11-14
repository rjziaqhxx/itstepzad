class AgeDescriptor:
    def __get__(self, instance, owner):
        print('Odczytuje dane')
        return self._age
    
    def __set__(self, instance, value):
        if 18 <= value <= 100:
            self._age = value
        else:
            raise ValueError('GOoogooo zazu')
        
class SalaryDescriptor:
    def __get__(self, instance, owner):
        print('Odczytuje dane')
        return self._salary
    
    def __set__(self, instance, value):
        if value >= 2000:
            self._salary = value
        else:
            raise ValueError('Gaaagaaa zazo')
    
class Employee:
    age = AgeDescriptor()
    salary = SalaryDescriptor()
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


obj = Employee('Josh', 35, 2100.35)
print('wiek ', obj.age,'pensja ', obj.salary,'imie ', obj.name)