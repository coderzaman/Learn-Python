# Abstraction involves hiding complex implementation details and exposing only the essential features of an object.
# It allows developers to focus on what an object does rather than how it does it.
import math
# Abstract Base Classes (ABC)
# Python provides the abc module to define abstract base classes, which cannot be instantiated and can enforce that derived classes implement specific methods.
# Non-abstract methods can exist in an abstract class.
# Abstract classes cannot be instantiated directly if they have any abstract methods.
# Subclasses must implement all abstract methods before they can be instantiated.

from abc import  ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def shape(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Usage
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

circle = Circle(10)
print(f'{circle.area():.2f}')
print(f'{circle.perimeter():.2f}')
