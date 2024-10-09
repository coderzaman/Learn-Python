# Basic Syntax
# [expression for item in iterable if condition]
# a. Creating a List of Squares
squares = [x**2 for x in range(1,11)]
print(squares)

print()
# Filtering Even Numbers
[print(even) for even in range(1,11) if even % 2 == 0 ]
even_numbers = [even for even in range(1,11) if even % 2 == 0 ]
print(even_numbers)
print()

# Applying a Function to Each Item

def square(x):
    return x * x

[print(square(x)) for x in range(1,11)]

print()

# Flattening a Nested List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flatted_list = [item for row in matrix for item in row]
print(flatted_list)


flatted_list_even = [item for row in matrix for item in row if item % 2 == 0]
print(flatted_list_even)

# Nested List Comprehensions
############################
###### Important Notes #####
###########################

# Order of for Clauses:
# • In single list comprehensions with multiple for clauses, the for clauses are ordered from outer to inner, just like nested for loops.
# Syntax
# [expr for x in outer for y in inner]  # x is outer, y is inner
# • In nested list comprehensions, each list comprehension can have its own for clauses, with the outer list comprehension controlling the outer loop and the inner list comprehension controlling the inner loop.
# Syntax
# [[expr for inner_var in inner_iterable] for outer_var in outer_iterable]


# Example: Transposing a Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose)

print()
# Creating a Matrix
matrix = [[1 for _ in range(4)] for  _ in  range(3)]
print(matrix)


