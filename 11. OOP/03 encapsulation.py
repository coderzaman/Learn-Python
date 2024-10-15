# Encapsulation is the bundling of data and methods that operate on that data within one unit (class).
# It restricts direct access to some of an object's components, which is a means of preventing accidental interference and misuse.


# In Python, private attributes and methods are indicated by a leading underscore (_) or double underscores (__). However, Python does not enforce strict access control; it's a convention to indicate intended privacy.
     # Single Underscore (_): Indicates that the attribute or method is intended for internal use (protected).
     # Double Underscore (__): Triggers name mangling to make it harder to access the attribute or method from outside the class.


# Example:

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__salary = 50000


    def get_salary(self):
        return self.__salary

    def __private_method(self):
        print("This is a private Method")

p = Person("Abdullah", 26)

print(p.name)
print(p._age) #not Recommended
print(p.get_salary())

# Accessing via name mangling
p._Person__private_method() #not recommended
p._Person__salary = 4000000
print(p._Person__salary)

# Mangling in Python is indeed a built-in feature designed to avoid unwanted access or conflicts by renaming private attributes and methods.
# Accessing these mangled names is possible, but it's not recommended because it goes against the intended use of encapsulation.
# When we defined private attribute or method it changes to private method or attribute to _className.__methodName() or _className.__attribute_name