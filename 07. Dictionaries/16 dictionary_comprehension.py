# Similar to list and set comprehensions, dictionary comprehensions provide a concise way to create dictionaries based on existing iterables.
# Creating a Dictionary of Squares:

squares = {x:x**2 for x in range(1,6)}
print(squares)

#filtering Item
squares = {x:x**2 for x in range(1,6) if x%2 == 0}
print(squares)

# Swapping Keys and Values:

original = {"a": 1, "b": 2, "c": 3}

swap_dic = {value:key for key,value in original.items()}
print(swap_dic)