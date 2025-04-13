# Multiple Inheritance : inherit from more than one parent class
                        #  C(A, B)
# Multilevel Inheritance : inherit from a parent which inherits from another parent
                        #    C(B) <-- B(A) <-- A


class Animals:
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

    def __init__(self, name):
        self.name = name

class Prey(Animals):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animals):
    def hunt(self):
        print(f'{self.name} is hunting')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
rabbit.flee()
rabbit.eat()
rabbit.sleep()

hawk = Hawk("Tony")
hawk.hunt()
hawk.eat()
hawk.sleep()

fish = Fish("Nemo")
fish.flee()
fish.hunt()
fish.eat()
fish.sleep()