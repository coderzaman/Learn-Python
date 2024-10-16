# Properties allow you to manage the access to instance attributes by defining methods that get, set, or delete their values.
# They provide a way to add logic around getting or setting an attribute, enforcing encapsulation.

# Using @property Decorator
# The @property decorator transforms a method into a "getter" for a read-only attribute.

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'



# Uses
person =  Person("Abdullah", "Abdur Rahman")
print(person.full_name)

# person.full_name = "Jane Smith"  # AttributeError: can't set attribute

print()

# Setting a Property with @<property>.setter
# To allow setting the value, define a setter method using @<property>.setter.

# Example:
class Person1:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ',1)
        self.first_name = first_name
        self.last_name = last_name

#Usage
p = Person1("Abu", "Huraira")
print(p.full_name)

p.full_name = "Abu Abdullah"
print(p.full_name)

print()

# Deleting a Property with @<property>.deleter
# You can also define a deleter method to handle attribute deletion.

class Person2:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split(' ', 1)
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print("Delete Full Name")
        del self.first_name
        del self.last_name


#Usage
p = Person2("Abu", "Huraira")
print(p.full_name)

p.full_name = "Abu Abdullah"
print(p.full_name)

# Attempting to access attributes after deletion
del p.full_name
# print(p.first_name) # AttributeError
# print(p.full_name) # AttributeError