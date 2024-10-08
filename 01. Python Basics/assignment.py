# Addition Assignment (+=)
x = 5
y = 3
x += y  # Equivalent to x = x + y
print(x)  # Output: 8

# b. Subtraction Assignment (-=)
x = 10
y = 4
x -= y  # Equivalent to x = x - y
print(x)  # Output: 6


# Floor Division Assignment (//=)
x = 9
y = 2
x //= y  # Equivalent to x = x // y
print(x)  # Output: 4


# Modulus Assignment (%=)
x = 10
y = 3
x %= y  # Equivalent to x = x % y
print(x)  # Output: 1


# Exponentiation Assignment (**=)
x = 2
y = 3
x **= y  # Equivalent to x = x ** y
print(x)  # Output: 8


# Bitwise Assignment Operators (&=, |=, ^=, <<=, >>=)
x = 5      # Binary: 0101
y = 3      # Binary: 0011

x &= y     # Binary AND: 0001
print(x)   # Output: 1

x = 5
x |= y     # Binary OR: 0111
print(x)   # Output: 7

x = 5
x ^= y     # Binary XOR: 0110
print(x)   # Output: 6

x = 5
x <<= 1    # Left shift: 1010 (10 in decimal)
print(x)   # Output: 10

x = 5
x >>= 1    # Right shift: 0010 (2 in decimal)
print(x)   # Output: 2

# Unpacking Assignments
# Tuple Unpacking
point = (10, 20)
x, y = point
print(x,y)

# List Unpacking
colors = ["red", "green", "blue"]
first, second, third = colors
print(first, second, third)

# Dictionary Unpacking
person = {"name": "Alice", "age": 30}
key1, key2 = person
print(key1, key2)

value1, value2 = person.values()
print(value1, value2)

(k1, v1), (k2, v2) = person.items()
print(k1,v1)
print(k2, v2)

# Key Points:
# Matching Structure
# This will raise a ValueError
# a, b = [1, 2, 3]

# Using Asterisk (*) for Variable-Length Unpacking:
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first,middle,last)

# Best Practices for Assignment Operators

# Avoid Chained Assignments with Mutable Objects:
# Risky
list1 = list2 = []

# Safer
list1 = []
list2 = []

# Use multiple assignments to make parallel assignments clear.
x, y, z = 1, 2, 3


# Advanced Topics

# a. Destructuring with Star Expressions
# Python allows the use of the asterisk (*) in unpacking to capture multiple values.

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5

*head, second, tail = numbers
print(head)    # Output: [1, 2, 3]
print(second)  # Output: 4
print(tail)    # Output: 5

head, second, *tail = numbers
print(head)    # Output: 1
print(second)  # Output: 3
print(tail)    # Output: [3, 4, 5]


# b. Nested Unpacking
# Unpack nested structures with multiple levels.

data = ("Alice", (25, "Engineer"), ["Python", "Data Science"])

name, (age, occupation), skill = data

print(name, age,occupation, skill)

# c. Augmented Assignment with Immutable Types
# For immutable types (like integers, strings, tuples), augmented assignments create new objects.
x = 5
print(id(x))  # Example Output: 140735192722208

x += 1
print(x)      # Output: 6
print(id(x))  # Example Output: 140735192722240 (different from previous)

# Strings
s = "Hello"
print(id(s))  # Example Output: 140735192723456

s += " World"
print(s)      # Output: Hello World
print(id(s))  # Example Output: 140735192724032 (different from previous)

#d The exec() and eval() Functions
# These functions can execute dynamically created assignment statements, though their use is generally discouraged due to security risks.
exec("a = 5")
print(a)

expr = "3-5"
print(eval(expr))