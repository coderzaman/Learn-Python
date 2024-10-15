# In hierarchical inheritance, multiple classes inherit from a common base class.
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class1


class Boy(Parent):
    def func2(self):
        print("This function is in Boy.")


# Derivied class2
class Girl(Parent):
    def func3(self):
        print("This function is in Girl.")



# Driver's code
object1 = Boy()
object2 = Girl()

object1.func1()
object1.func2()

object2.func1()
object2.func3()