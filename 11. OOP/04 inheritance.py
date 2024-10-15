# Inheritance allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass).
# It promotes code reusability and establishes a natural hierarchy between classes.


class Person:
    def __init__(self, name, age):
        print("Something")
        self.name = name
        self.age = age
    def information(self):
        print(f'Name: {self.name}, Age:{self.age}')

class Employee(Person):
    def __init__(self, name, age, emp_id, position):
        self.emp_id = emp_id
        self.position = position
        super().__init__(name, age)


    def information(self):
        print(f'Employee Id:{self.emp_id}, Name:{self.name}, Age:{self.age}, Position: {self.position}')


person = Person("Abdullah", 26)
person.information()

employee = Employee(person.name, person.age, 1, "Programmer")
employee.information()