# Generator expressions are similar to list comprehensions but use parentheses () instead of brackets [].
# They generate items one at a time and are more memory-efficient, making them suitable for large datasets.

# Basic Syntax
# (expression for item in iterable if condition)

# Examples
# a. Creating a Generator for Squares
square = (x**2 for x in range(1,11))
print(square)

# To retrieve the items, you can iterate over the generator:
for x in square:
    print(x)
print()
# b. Filtering with a Generator Expression
even_number  =  (even_number for even_number in range(1,11) if even_number % 2 == 0)
for num in even_number:
    print(num)

print()

# Using next() with Generators
# You can manually retrieve items using the next() function
squares_gen = (x**2 for x in range(5))
print(next(squares_gen))  # Output: 0
print(next(squares_gen))  # Output: 1

print()

# Memory Efficiency Example
# Creating a large list vs. a generator:

# List comprehension
large_list = [x for x in range(1000000)]

# Generator expression
large_gen = (x for x in range(1000000))

# List Comprehension: Allocates memory for the entire list.
# Generator Expression: Generates items on-the-fly, using much less memory.
