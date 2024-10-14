# Tuple unpacking allows you to assign the elements of a tuple to individual variables in a single statement.
# Unpacking a tuple
person = ("Alice", 30, "Engineer")

name, age, profession = person
print(name)       # Output: Alice
print(age)        # Output: 30
print(profession) # Output: Engineer

# Error Example (Mismatch in Elements):
data = (1, 2, 3)
# a, b = data  # ValueError: too many values to unpack (expected 2)

# Handling Variable Number of Elements:
# Using * to capture remaining elements
data = (1, 2, 3, 4, 5)
a, b, *c = data
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: [3, 4, 5]

# Packing Tuples
# Tuple packing
packed = "x", "y", "z"
print(packed)  # Output: ('x', 'y', 'z')

# Equivalent to
packed = ("x", "y", "z")
print(packed)  # Output: ('x', 'y', 'z')

#
# Swapping Variables
# Tuples make it easy to swap the values of two variables without needing a temporary variable.
a = 10
b = 20

# Swapping using tuple unpacking
a, b = b, a

print(a)  # Output: 20
print(b)  # Output: 10

data = (1, 2, 3, 4, 5)
*a, b, c,d = data
print(a,b,c,d)