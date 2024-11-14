#property decorators
class Rectangle:
    def __init__(self, width):
        self._width = width
        
    #getter
    @property
    def width(self):
        return self._width
    
    #setter
    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Width must be positive')
        
    @property
    def area(self):
        return self._width ** 2
    
rect = Rectangle(4)
print(rect.area)
rect.width = 10
print(rect.area)

try:
    rect.width = -3
except ValueError as e:
    print(e)