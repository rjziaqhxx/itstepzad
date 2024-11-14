class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        """The age of the person is years"""
        return self._age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('Googoo zaza')
        self._age = value

    @age.deleter
    def age(self):
        print('Deleting age...')
        del self._age

person = Person('Ice', '52')
print(person._age)

#setter
person.age = 35
print(person._age)
print(Person.age.__doc__)

#deleter
del person.age

