# Inheritance in Python = Allows a class to inherit attributes and methods
                        # from another class helps with code reusability and extensibility
                        # class Child(Parent)
                        # class subclass(superclass)

class Animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animals):
    def speak(self):
        print("Woof!")

class Cat(Animals):
    def speak(self):
        print("MEOW!")

class Mouse(Animals):
    def speak(self):
        print("SQUEEK!")


dog = Dog("Sheru")
cat = Cat("Tobby")
mouse = Mouse("Mickey")

print(f"{dog.name} : {dog.is_alive}")
dog.eat()
dog.sleep()
dog.speak()
print(f"{cat.name} : {cat.is_alive}")
cat.eat()
cat.sleep()
cat.speak()
print(f"{mouse.name} : {mouse.is_alive}")
mouse.eat()
mouse.sleep()
mouse.speak()