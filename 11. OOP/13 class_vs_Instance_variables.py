# Class Variables
# Definition: Variables that are shared among all instances of a class.
# Usage: To store data that should be consistent across all instances.
# Access: Via the class name or via instances.


# Example:  Class variables are shared across all instances of the class, while instance variables are unique to each instance.
# When you modify the class variable using the class name, the change reflects across all instances, old and new.
class Employee:
    # Class variable
    company = "ABC Corp"

    def __init__(self, name):
        self.name = name  # Instance variable


# Usage
emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(emp1.company)  # Output: ABC Corp
print(emp2.company)  # Output: ABC Corp

# Modifying class variable via the class
Employee.company = "XYZ Inc"
print(emp1.company)  # Output: XYZ Inc
print(emp2.company)  # Output: XYZ Inc

em3 = Employee("ABC")
print(em3.company)

print()
# Instance Variables
# Definition: Variables that are unique to each instance of a class.
# Usage: To store data that varies between instances.
# Access: Only via instances.

# Example:
class Employee:
    def __init__(self, name, salary):
        self.name = name      # Instance variable
        self.salary = salary  # Instance variable

# Usage
emp1 = Employee("Alice", 70000)
emp2 = Employee("Bob", 80000)

print(emp1.name)    # Output: Alice
print(emp2.name)    # Output: Bob

print(emp1.salary)  # Output: 70000
print(emp2.salary)  # Output: 80000

print()
# Important Notes
# Class Variable Overridden by Instance Variable: If an instance variable shares the same name as a class variable, the instance variable takes precedence.
class Employee:
    company = "ABC Corp"

    def __init__(self, name):
        self.company = "Personal Project"  # Overrides class variable for this instance


emp = Employee("Charlie")
print(emp.company)  # Output: Personal Project
print(Employee.company)  # Output: ABC Corp

print()
# Accessing Class Variables: Access class variables using the class name to avoid confusion with instance variables.
class Employee:
    company = "ABC Corp"

    def __init__(self, name):
        self.name = name


emp = Employee("Diana")
print(Employee.company)  # Output: ABC Corp
print(emp.company)  # Output: ABC Corp
