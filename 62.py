# class variables : Shared among all instances of class
                    # Defined outside the constructor
                    # Allow you the share data among all objects created from that class


# instance variable are defined inside the constructor
# class variable are defined outside the constructor
class Car:
    wheel = 4
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Students:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.num_students+=1

stud1 = Students("spongebob", "30")
stud2 = Students("Patrick", "28")
stud3 = Students("Squidward", "32")
stud4 = Students("Sandy", "25")

print(stud1.name)
print(stud1.age)
# print(stud1.class_year)
print(Students.class_year)

print(stud2.name)
print(stud2.age)
# print(stud2.class_year)
print(Students.class_year)

print(f"The number of students = {Students.num_students}")