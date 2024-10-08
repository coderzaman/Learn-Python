# Nested lists are lists within lists, allowing you to create multi-dimensional data structures.

# Examples:
# Creating a nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
# Output:
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Accessing elements in a nested list
print(matrix[0][1])  # Output: 2 (first row, second column)
print(matrix[2][0])  # Output: 7 (third row, first column)

# Modifying an element
matrix[1][2] = 60
print(matrix)
