# Class methods : Allow operations related to the class itself
                # Take (cls) as the first parameter, which represents the class itself


# instance method : best for operation on instances of the class (object)
# static methods : best for utility functions that do  not need acess to class data
# class methods : best for class-level data or require access to the class itself

class Student:
    count = 0
    total_cgpa = 0
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        Student.count +=1 
        Student.total_cgpa +=self.cgpa
    
    def get_info(self):
        return f"{self.name}, {self.cgpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of student : {cls.count}"
    
    @classmethod
    def get_avg(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average cgpa = {cls.total_cgpa/cls.count:.2f}"


student1 = Student("Anup", 8.3)
student2 = Student("Aryan", 8.9)
student3 = Student("Sharan", 7.7)

print(Student.get_count())
print(Student.get_avg())