# Accessing Values
# You can access dictionary values using their corresponding keys:
from os import pread

# Using Square Brackets []:
person = {"name": "Alice", "age": 30, "profession": "Engineer"}
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 30
print()

# Note: Accessing a non-existent key using [] raises a KeyError.
# print(person["salary"])  # Raises KeyError: 'salary'


# Using the .get() Method:
# Avoids KeyError by returning None or a specified default value if the key is not found.

print(person.get("name"))
print(person.get("salary")) # Return None If item not exist in dictionary
print()

# You can use get function for unknown/undeclared key. get(key, value) returns the value. But it not add item on original dictionary
print(person.get("Salary", 70000))
print(person)


