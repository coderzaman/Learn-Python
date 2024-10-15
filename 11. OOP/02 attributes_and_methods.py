# Attributes:
# Attributes are variables that belong to a class or its instances.
    # Class Attributes: Shared across all instances of the class.
    # Instance Attributes: Unique to each instance.
from datetime import datetime

from dateutil.utils import today


class Car:
    # class attribute
    wheels = 4

    #constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return self.brand, self.model


#Creating Instances
car1 =  Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.get_info()[0], car1.get_info()[1])
print(car2.get_info()[0], car2.get_info()[1])

print()

print(car1.wheels)
print(car2.wheels)

# Methods:
# Methods are functions defined within a class that describe the behaviors of the objects.
#     Instance Methods: Operate on instance attributes.
#     Class Methods: Operate on class attributes and are marked with the @classmethod decorator.
#     Static Methods: Do not operate on class or instance attributes and are marked with the @staticmethod decorator.


# Example of Instance Method:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Instance Method
    def area(self):
        return self.width * self.height


rect = Rectangle(5,10)
print(rect.area())

# class Method
class Bus:
    def __init__(self, name, route, capacity):
        self.name = name
        self.route = route
        self.capacity = capacity

    #class Method
    @classmethod
    def get_info(cls, bus):
        print(bus.name, bus.route, bus.capacity)


bus1 = Bus("Green Line", "Dhaka <=> Cox's Bazar", 40)
bus2 = Bus("Unique", "Dhaka <=> Sylhet", 30)
print()
bus1.get_info(bus1)
bus1.get_info(bus2)

print()

# Static Method
from dateutil.relativedelta import relativedelta

class Dateutil:
    @staticmethod
    def get_age(birth_date):
        current_date = datetime.now()
        age = relativedelta(current_date, birth_date)
        return age

birthdate = datetime(1998,4,13)
age = Dateutil.get_age(birthdate)

print(f'{age.years} Years, {age.months}, {age.days}')
