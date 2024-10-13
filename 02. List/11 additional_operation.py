# a. index() Method
# Finds the first index of a specified value. Raises a ValueError if the value is not found.

# Syntax:
# index = my_list.index(value, start, end)

# start (optional): Start searching from this index.
# end (optional): Stop searching before this index.


fruits = ["apple", "banana", "cherry", "banana", "date"]
index_banana = fruits.index("banana")
print(index_banana)

index_banana = fruits.index("banana", 2, 5)
print(index_banana)

# index_banana = fruits.index("banana", 2, 5) #Value error


# b. reverse() Method
# Reverses the elements of the list in place.

# Syntax:
fruits.reverse()
print(fruits)