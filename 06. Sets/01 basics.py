# Creating Sets

# Using Curly Braces {}:
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Using the set() Constructor
fruits_string = "Apple Orange Banana Jackfruit Apple"
fruits_list = set(fruits_string.split())
print(fruits_list)

# Using Set Comprehensions:
number_set = {number for number in range(1,11)}
print(number_set)

# Important Notes:
# Uniqueness: When creating a set, duplicate elements are automatically removed.
duplicates = {1, 2, 2, 3, 4, 4, 5}
print(duplicates)

# Immutable Elements: Sets cannot contain mutable elements like lists or dictionaries.
# This will raise a TypeError
# invalid_set = {1, 2, [3, 4]}
# TypeError: unhashable type: 'list'

# Set Immutability
# While sets themselves are mutable (you can add or remove elements), the elements within a set must be immutable (hashable).
#

# Attempting to add a list to a set
# s = {1, 2, 3}
# s.add([4, 5])  # Raises TypeError: unhashable type: 'list'

# Immutable Elements (Allowed):
my_set = set((1, 2, 3, 4, 5, 6))
print(my_set)

my_set.add((5,6,7,8,9))
print(my_set)

# Set Indexing and Slicing
# Sets are unordered, which means they do not support indexing, slicing, or other sequence-like behavior.
s = {"apple", "banana", "cherry"}

# Attempting to access an element by index
# print(s[0])  # Raises TypeError: 'set' object is not subscriptable

# Iterating through a set
for fruit in s:
    print(fruit)

# Set Concatenation and Repetition
# Sets do not support concatenation (+) or repetition (*) operations like lists and strings because they are unordered and contain unique elements.
s1 = {"a", "b", "c"}
s2 = {"d", "e", "f"}

# Concatenation (Not Supported)
# combined = s1 + s2  # Raises TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Repetition (Not Supported)
# repeated = s1 * 2  # Raises TypeError: unsupported operand type(s) for *: 'set' and 'int'

# Single-Element Sets
# To create a set with a single element, include a trailing comma inside the curly braces.
singleton = {"apple"}
print(singleton)
print(type(singleton))

# However, {} is an empty dictionary, not a set
empty = {}
print(type(empty))  # Output: <class 'dict'>

# Correct way for empty set
empty_set = set()
print(type(empty_set))  # Output: <class 'set'>