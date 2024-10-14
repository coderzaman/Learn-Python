# Basic Syntax:
# new_list = [expression for item in iterable if condition]
import time

# Examples:
# Square Number 2 to 10
squares = [(x+2)**2 for x in range(12)]
print(squares)

even_number = [x for x in range(10) if x % 2 == 0]
print(even_number)


# Create a list of uppercase fruits
fruits = ["apple", "banana", "cherry"]

upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# make flattened list
flatted_list = [item for sublist in matrix for item in sublist]
print(flatted_list)

# make even flatted list
flatted_list = [item for sublist in matrix for item in sublist if item % 2 == 0]
print(flatted_list)

