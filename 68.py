'''
Static methods = A method that belongs to a class rathar than any object from that class (instance)
                 usually used for general utility functions

Instances methods = Best for operation on instances of the class(objects)
Static methods = best for utility functions that do not need access to class data
'''


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions
    
employee1 = Employee("Anup", "Manager")
print(Employee.is_valid_position(employee1.position))

print(employee1.get_info())