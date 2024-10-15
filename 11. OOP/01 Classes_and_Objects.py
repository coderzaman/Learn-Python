# A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.
# Syntax:
"""

class ClassName:
    # Class attributes
    class_attribute = value

    # Constructor method
    def __init__(self, parameters):
        # Instance attributes
        self.instance_attribute = value

    # Methods
    def method_name(self, parameters):
        # Method body
        pass

"""

class Dog:
    """A simple Dog Class"""

    # class attribute
    species = "Canis Familiaris"

    # Constructor
    def __init__(self, name, age):
        # Instance Attribute
        self.name = name
        self.age = age

    # Method
    def bark(self):
        return f"{self.name} says Woof!"



dog1 = Dog("Buddy",5)
print(dog1.bark())
print(dog1.name)
print(dog1.age)

print()
dog2 = Dog("JIGO",5)
dog1 = Dog("Buddy",5)
print(dog1.bark())
print(dog1.name)
print(dog1.age)