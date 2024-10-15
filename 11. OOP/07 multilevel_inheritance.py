# In multilevel inheritance, a class inherits from another class, and then a third class inherits from the second class.

class Shape:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def is_shape(self):
        if self.__height > 0 and self.__width > 0:
            print("it's a shape")


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height,width)

class Circles(Rectangle):
    def __init__(self, height, width, radius):
        self.radius = radius
        super().__init__(height, width)

circle = Circles(1,4,5)
rect = Rectangle(1,5)

rect.is_shape()
circle.is_shape()
