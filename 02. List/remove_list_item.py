# a. remove() Method
# Syntax: list.remove(value)
from os import pread

fruits = ["apple", "banana", "cherry", "banana", "date"]
fruits.remove("apple")

print(fruits)

# If not exist in the list
# fruits.remove("apple") #ValueError: list.remove(x): x not in list


# b. pop() Method
# Removes an item at a specified index and returns it. If no index is specified, it removes and returns the last item  or specified index item.
# Syntax:

# item = my_list.pop(index) default index is last item index in list

numbers = [10, 20, 30, 40, 50]
remove_item = numbers.pop(1)
print(remove_item)
print(numbers)


# del Statement
# del my_list[index]
# del my_list[start:end]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Remove the item at index 1
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry', 'date', 'elderberry']

del fruits[0:2]
print(fruits)

del fruits[:]
print(fruits)

# d. clear() Method

# Syntax:
# my_list.clear()

# Example:
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Output: []
