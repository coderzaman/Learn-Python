# An empty list
empty_list = []

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.14, True]

# List of lists (nested list)
nested_list = [[1, 2], [3, 4], [5, 6]]


# Creating Lists Using the list() Constructor:
tuple_data = (1,"34","hello",34.3)
my_List = list(tuple_data)
print(type(my_List), my_List)


# From a string
string_data = "World"

# After converting string to list Each char of string should be an list Item
my_List = list(string_data)
print(my_List)


# with constructor
new_list = list([1,2,3,5])
print(new_list)