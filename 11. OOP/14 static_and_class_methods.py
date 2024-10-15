# Class Methods
# Definition: Methods that receive the class as the first argument, typically named cls.
# Decorator: @classmethod
# Use Cases: Factory methods, modifying class state.

class Employee:
    company = "ABC Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))


# Usage
emp1 = Employee("Alice", 70000)
print(emp1.company)  # Output: ABC Corp

# Changing company using class method
Employee.change_company("XYZ Inc")
print(emp1.company)  # Output: XYZ Inc

# Creating an instance using a factory class method
emp_str = "Bob-80000"
emp2 = Employee.from_string(emp_str)
print(emp2.name)  # Output: Bob
print(emp2.salary)  # Output: 80000
print(emp2.company)  # Output: XYZ Inc


# Static Methods
# Definition: Methods that do not receive an implicit first argument (neither self nor cls).
# Decorator: @staticmethod
# Use Cases: Utility functions that perform a task in isolation.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# Usage
print(MathOperations.add(5, 3))  # Output: 8
print(MathOperations.multiply(5, 3))  # Output: 15

# Can also be called via an instance
math_op = MathOperations()
print(math_op.add(2, 4))  # Output: 6

# Feature	        Instance Methods	                  Class Methods	                                Static Methods
# First Parameter	    self                	              cls	                                          None
# Access	         Via instances      	        Via class or instances	                         Via class or instances
# Use Cases	    Manipulate instance data	  Manipulate class data or create instances   	            Utility functions