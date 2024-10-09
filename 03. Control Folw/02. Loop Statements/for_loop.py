# Syntax
# for variable in sequence:
#     # Code block to execute for each item

# Example
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
print()
# Iterating Over Different Data Types
# a. List
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)

print()
# b. Tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)
print()

# c. Dictionary
student_ages = {"Alice": 25, "Bob": 22, "Charlie": 23}

for student in student_ages:
    print(student)
print()
# d. String
# Iterating over a string allows you to access each character individually.
word = "Python"

for letter in word:
    print(letter)
print()
# Using range() with for Loops

# a. Basic Usage
# print 0 to before numbers
print()
for x in range(5):
    print(x)

print()

# b. Specifying Start and End
# print start to end-1
for x in range(1,11):
    print(x)

print()

#c. Specifying Step
# print 1, end-1, with step+2
for x in  range(0,11,2):
    print(x)

print()

# Nested for Loops
# You can place one for loop inside another to handle multidimensional data structures.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for item_of_row in row:
        print(item_of_row, end=' ')
    print()

