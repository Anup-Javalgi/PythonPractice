# Ploymorphism in Python
'''
Greek word means to have many forms or faces of object
Poly = many
Morphe = Form

Two ways to achieve Polymorphism
Inheritance = An object could be treated of the same type as parent class
Duck typing = Object must have necessary attribute/methods
'''

from abc import ABC, abstractmethod

class Shapes(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2    

class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2
 
class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base*self.height*0.5


# class Pizza:
#     def __init__(self, topping, radius):
#         self.topping = topping
#         self.radius = radius

# class Pizza(Shapes):
#     def __init__(self, topping, radius):
#         self.topping = topping
#         self.radius = radius

class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)


# circle = Circle()  # circle is a circle and a shape (@ forms of circle)

shapes = [Circle(4), Square(3), Triangle(5, 6), Pizza("peperoni", 15)]

for shape in shapes:
    print(f"Area of {shape} = {shape.area()}cm^2")

print(type(Shapes))