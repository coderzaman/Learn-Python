# Multiple inheritance involves a class inheriting from more than one base class.
class Father:
    def __init__(self, father_name):
        self._father_name = father_name

    def father(self):
        print(f"Father name: {self._father_name}")


class Mother:
    def __init__(self, mother_name):
        self._mother_name = mother_name

    def mother(self):
        print(f"Father name: {self._mother_name}")

class Son(Father, Mother):
    def __init__(self, name, father_name, mother_name):
        self.name = name
        super().__init__(father_name)
        Mother.__init__(self, mother_name)


son = Son("Abdullah", "Abu Abdullah", "Ummo Abdullah")

print("Name: ", son.name)
son.father()
son.mother()
