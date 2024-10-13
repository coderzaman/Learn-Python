# Example 1: Returning Multiple Values from a Function
# Tuples are commonly used to return multiple values from a function.

def get_user_info():
    name = "Abdullah"
    age = 26
    profession = "Data Scientist"

    return name, age, profession

# user_name, age, profession = get_user_info()
name, age, profession = get_user_info()
print(name)        # Output: Eve
print(age)         # Output: 28
print(profession)


# Example 2: Using Named Tuples for Structured Data
# Named tuples enhance the readability and usability of tuples by allowing access via named fields.
from collections import namedtuple

# Define the named tuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=15, y=25)

print(p1)          # Output: Point(x=10, y=20)
print(p2.x, p2.y)  # Output: 15 25

print()

# Example 3: Swapping Variables Using Tuples
# Tuples simplify the process of swapping values between variables.

a = "first"
b = "second"

# Swapping using tuple unpacking
a, b = b, a

print(a)  # Output: second
print(b)  # Output: first


# Exercise 1: Finding Unique Elements
def unique_elements(t):
    return tuple(set(t))

numbers = (1, 2, 2, 3, 4, 4, 5)
unique = unique_elements(numbers)
print(unique)

# Exercise 2: Merging Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)

merged = t1 + t2
print(merged)

# Exercise 3: Reversing a Tuple
t = (1, 2, 3, 4, 5)
reversed_t = t[::-1]
print(reversed_t)  # Output: (5, 4, 3, 2, 1)

# Checking for an Element in a Tuple
t = ("apple", "banana", "cherry")

def contains(t, element):
    return element in t

print(contains(t, "banana"))  # Output: True
print(contains(t, "grape"))   # Output: False


# Exercise 5: Counting Vowels in a Tuple of Strings
# Task: Given a tuple of strings, count the total number of vowels present.
# Tuple: ("hello", "world", "python", "programming")


my_tuple = ("hello", "world", "python", "programming")

vowel = "aeiouAEIOU"
count = sum([1 for item in my_tuple for ch in item if ch in vowel])
print(count)