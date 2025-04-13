# super() : Function used in child class to call methods from parent class(superclass).
          # Alows you to extend the functionality of the inherited method.
          # Avoids method overriding and constructor overriding

class Shapes:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Its {self.color} and {'Filled' if self.is_filled else 'Not filled'}")

class Circle(Shapes):
    def __init__(self, color, is_filled, radius):
        # self.color = color
        # self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"Its a circle with an area {3.14*self.radius**2}cm^2")
        super().describe()

class Square(Shapes):
    def __init__(self, color, is_filled, width):
        # self.color = color
        # self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Its a square with an area {self.width**2}cm^2")
        super().describe()

class Triangle(Shapes):
    def __init__(self, color, is_filled, width, height):
        # self.color = color
        # self.is_filled = is_filled
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"Its a triangle with an area {(self.width*self.height)/2}cm^2")
        super().describe()


circle = Circle("white", True, 5)
square = Square("Yellow", True, 3)
triangle = Triangle("Sky blue", True, 6, 7)

print(circle.__dict__)
print(f"{circle.color}")
print(f"{circle.is_filled}")
print(f"{circle.radius}cm")
circle.describe()

print(square.__dict__)
print(f"{square.color}")
print(f"{square.is_filled}")
print(f"{square.width}cm")
square.describe()

print(triangle.__dict__)
print(f"{triangle.color}")
print(f"{triangle.is_filled}")
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()