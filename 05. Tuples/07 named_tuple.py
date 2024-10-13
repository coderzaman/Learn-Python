# Named Tuples
# Named Tuples provide a way to define simple classes with named fields, making tuples more readable and accessible.
#
# Advantages:
#
# Access elements by name instead of index.
# Improves code readability.
# Immutable like regular tuples.

#Creating Named Tuples:
# Using the collections module:

from collections import namedtuple

# Define name tuple type

Person = namedtuple("Person", ['name','age','profession'])

alice = Person(age=26,name="Alice",profession="Developer")
print(alice[0], alice.name)

abdullah = Person("Abdullah", 27, "Programmer")
print(abdullah.name)
print(abdullah[1])
print(abdullah.profession)

# Extending Named Tuples:
Employee = namedtuple("Employee", Person._fields + ('employee_id',))

abu_huraira = Employee('Abu Huraira', 26, 'Developer', 1001)
print(abu_huraira.name, abu_huraira.age, abu_huraira.profession, abu_huraira.employee_id)


