# a. Using the + Operator


list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)  # Output: [1, 2, 3, 4, 5, 6]

# Using the extend() Method
print(id(list1))
list1.extend(list2)
print(list1)

# c. Using the * Operator (Replicating Lists)
# The * operator can be used to repeat a list multiple times.
# Syntax:
# repeated_list = my_list * n

letters = ["a","b","c"]
numbers = [1, 2, 3]

repeated_list = letters * 3
print(repeated_list)

repeated_list = numbers * 3
print(repeated_list)


# d. Using List Comprehensions
concatList = [item for sublist in [list1, list2] for item in sublist]
print(concatList)

# e. Using the itertools Module
# For more advanced list joining, the itertools module provides tools like chain().
import itertools
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

combined = list(itertools.chain(list1,list2,list3))
print(combined)

