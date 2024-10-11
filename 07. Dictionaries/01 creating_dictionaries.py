# Creating Dictionaries
# Using Curly Braces {}:
# Empty dictionary

empty_dict = {}
print(empty_dict)

print()
# Dictionary with key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "profession": "Engineer"
}
print(person)
print()

# Using the dict() Constructor:
car = dict(make="Toyota", model="Camry", year=2000)
print(car)
print()

#From a list of tuples:
car = dict([("make", "Toyota"), ("model","Camry"), ("year", 2000)])
print(car)
print()

#from List of List
car = dict([["make", "Toyota"], ["model", "Camry"], ["year", 2000]])
print(car)
print()

my_tuple = (("make", "Toyota"), ("model", "Camry"), ("year", 20000))
print(type(my_tuple))
print()

car = dict(my_tuple)
print(type(car))
print(car)

print()

# Using Dictionary Comprehensions
squares = {x: x**2 for x in range(1,6)}
print(squares)

# If you can add multiple item with same key name it selected last key item value
person = {"name": "Alice", "age": 30, "name": "Abdulalah"}
print(person)

