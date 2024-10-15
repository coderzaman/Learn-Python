# Polymorphism allows objects of different classes to be treated as objects of a common superclass.
# It enables methods to perform different tasks based on the object it is acting upon.


# Example: Method overloading
class Bird:
    def fly(self):
        return "Flying"

class Airplane(Bird):
    def fly(self):
        return "Airplane is Flying"

def make_it_fly(flyable):
    print(flyable.fly())


bird = Bird()
airplane = Airplane()

make_it_fly(bird)
make_it_fly(airplane)

#Operator Overloading

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z+ other.z)


    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.y})"


v1 = Vector(2,4,3)
v2 = Vector(2,3,4)


v3 = v1 + v2 + v1
print(v3)