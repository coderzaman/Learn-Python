# a. Shallow Copy
# A shallow copy creates a new list object but does not create copies of nested objects.
# Instead, it references the same nested objects.

# Methods to Create a Shallow Copy:
#
# Using the copy() method
# Using slicing [:]
# Using the list() constructor

original = [1, 2, [3, 4]]
print(original)

copy_list = original.copy()
print(copy_list)

original.append(10)
print(original)
print(copy_list)

original[2].append(10)
print(copy_list)
print(original)

# Nested Object refer to same object in shallow copy
print(id(original[2]))
print(id(copy_list[2]))


# print(id(original), id(copy_list))

# b. Deep Copy
# A deep copy creates a new list and recursively copies all nested objects, resulting in complete independence from the original list.
#

# Method to Create a Deep Copy:
# A deep copy creates a new list and recursively copies all nested objects, resulting in complete independence from
# the original list.

# Method to Create a Deep Copy:
# Using the deepcopy() function from the copy module

import copy

original = [1, 2, [3, 4]]

deep_copy = copy.deepcopy(original)

# Modifying the deep copy does not affect the original
deep_copy[2].append(5)
print(original)   # Output: [1, 2, [3, 4]]
print(deep_copy)  # Output: [1, 2, [3, 4, 5]]

# Deep copy does not same memory address of nested list
print(id(original[2]) == id(deep_copy[2]))
