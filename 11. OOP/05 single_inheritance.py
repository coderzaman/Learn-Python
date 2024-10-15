# In single inheritance, a class inherits from only one base class.
class Animal:
    def speak(self):
        print("Animal an speak")

class Cat(Animal):
    def meow(self):
        print("Cat say something to you! Meow")

cat = Cat()
cat.meow()