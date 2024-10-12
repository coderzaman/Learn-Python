# Lambda functions are small, unnamed functions defined using the lambda keyword. They are primarily used for short, throwaway functions.
# Syntax:
# lambda arguments: expression


# Example
add = lambda a,b: a+b
print(add(3,4))
print()

# Sorting with Custom Keys:
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_student = sorted(students, key = lambda student:student[1])
print(sorted_student)
print()

# Using with map(), filter()
numbers = [1, 2, 3, 4, 5]

squares_numbers = list(map(lambda x: x**2, numbers))
print(squares_numbers)
print()

# Using filter to get even numbers
even = list(filter(lambda x:x%2==0, numbers))
print(even)
print()

from functools import reduce
# Using reduce to compute the product
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

