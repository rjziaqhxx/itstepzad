class Shape:
    def __area__(self):
        return 'Undefined area'
    
    def __str__():
        return 'Shape'
    
class Colored:
    def __init__(self, color):
        self.color = color
    
    def __str__():
        return 'Colored'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def __area__(self):
        new = self.radius * self.radius
        return 3.14 * new
    
class ColoredCircle(Circle, Colored):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    
    def __str__(self):
        return f'Colored circle of color {self.color}'

    def __add__(self, other):
        new_radius = self.radius + other.radius
        if self.color == other.color:
            return new_radius, self.color
        else:
            return new_radius, 'mixed'   

    def __nul__(self, other):
        new_radius = self.radius * other
        return round(new_radius, 2)
    
    def __eq__(self, other):
        if self.radius == other.radius and self.color == other.color:
            return True
        return False
    
obj = ColoredCircle(10,'black')

obj2 = ColoredCircle(10,'black')



new = obj.__add__(obj2)
print(new)
print(obj == obj2)
