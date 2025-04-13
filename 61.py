# Object oriented programming in python
'''
Object = A bundle of related attributes (variables) and methods (functions)
         Ex: phone, cup, book
         you need a class to create many objects

class = (blueprint) used to design the structure and layout of an object
'''

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
            print(f"You drive the {self.model}")
        
    def stop(self):
            print(f"You stop the car {self.model}")

    def describe(self):
          print(f"{self.year} { self.color} {self.model}")



car1 = Car("Lamborgini", 2024, "black mat", False)
car2 = Car("Rolls-Royce", 2024, "White", False)


print(car1)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
car1.describe()
car1.drive()
car1.stop()

print(car2)

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
car2.describe()
car2.drive()
car2.stop()