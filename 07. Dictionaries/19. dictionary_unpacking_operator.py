# In Python, the ** operator is known as the dictionary unpacking operator.
# Syntax: merged = {**dict1, **dict2}
# {}: Denotes a dictionary literal.
# **dict1: Unpacks all key-value pairs from dict1 into the new dictionary.
# **dict2: Unpacks all key-value pairs from dict2 into the new dictionary.
# merged: The resulting dictionary containing combined key-value pairs from both dict1 and dict2.
from doctest import Example

# Example
# Define two dictionaries
dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "b": 20,
    "d": 4
}

# Merge dictionaries using ** unpacking
merged = {**dict1, **dict2}

print(merged)
# Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}


print()

# Merging Multiple Dictionaries
# You can merge more than two dictionaries by chaining the ** operator:

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}
dict3 = {"c": 30, "d": 4}

merged = {**dict1, **dict2, **dict3}

print(merged)
# Output: {'a': 1, 'b': 20, 'c': 30, 'd': 4}

print()

# Comparison with Other Merging Methods
# Using the .update() Method
# Another common way to merge dictionaries is using the .update() method. However, there are key differences:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

# Using .update() modifies dict1 in-place
dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 20, 'c': 3}



# Example
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 20, "c": 3}

# Using ** unpacking
merged = {**dict1, **dict2}
print(merged)
# Output: {'a': 1, 'b': 20, 'c': 3}

print(dict1)
# Output: {'a': 1, 'b': 2}  # Unchanged

# Using .update()
dict1.update(dict2)
print(dict1)
# Output: {'a': 1, 'b': 20, 'c': 3}  # Modified

print()

# Order Matters: In cases where multiple dictionaries have the same keys, the last dictionary's value for that key will prevail.
dict1 = {"x": 1}
dict2 = {"x": 2}
dict3 = {"x": 3}

merged = {**dict1, **dict2, **dict3}
print(merged)
# print()


# Non-Dictionary Iterables
# Using .update() with an iterable of tuples
dict1 = {"a": 1}
dict1.update([("b", 2), ("c", 3)])
print(dict1)
# Output: {'a': 1, 'b': 2, 'c': 3}

# Using ** unpacking with non-dictionary iterables raises TypeError
try:
    merged = {**dict1, **[("d", 4)]}
except TypeError as e:
    print(e)  # Output: 'mapping expected instead of list'

# Example 1: Merging Dictionaries with Overlapping Keys
dict1 = {"name": "Alice", "age": 25, "city": "New York"}
dict2 = {"age": 30, "profession": "Engineer"}

merged = {**dict1, **dict2}
print(merged)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'profession': 'Engineer'}

print()

# Example 2: Merging Dictionaries with No Overlapping Keys
dict1 = {"fruit": "apple"}
dict2 = {"vegetable": "carrot"}

merged = {**dict1, **dict2}
print(merged)
print()


# Example 3: Merging Dictionaries in a Function
def merge_dict(*dicts):
    merge = {}
    for dic in dicts:
        merge = {**merge, **dic}
    return merge

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
dict_c = {"c": 5, "d": 6}

result = merge_dict(dict_a,dict_b,dict_c)

print(result)
print()

# Example 4: Merging Dictionaries with Variable Keys
defaults = {
    "host": "localhost",
    "port": 8080,
    "debug": False
}

overrides = {
    "port": 9090,
    "debug": True
}

config = {**defaults, **overrides}
print(config)
# Output: {'host': 'localhost', 'port': 9090, 'debug': True}
print()

# Example: Unpacking in Function Calls
#paramenter value must be same with object key, order of key is not mandatory
def greet(age, name):
    print(f'Hello, {name}! Your age is {age} old')

info = {"name": "Abdullah", "age":26}

greet(**info)