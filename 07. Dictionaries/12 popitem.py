# Removes and returns an arbitrary key-value pair as a tuple. As of Python 3.7, it removes the last inserted key-value pair.

person = {"name": "Alice", "age": 30, "profession": "Engineer"}

# Popping the last item
item = person.popitem()
print(item)   # Output: ('profession', 'Engineer')
print(person) # Output: {'name': 'Alice', 'age': 30}

# Note: Attempting to pop from an empty dictionary raises a KeyError.
empty_dict = {}
# empty_dict.popitem()  # Raises KeyError: 'popitem(): dictionary is empty'
