# Returns a view object containing all key-value pairs as tuples.
person = {"name": "Alice", "age": 30, "profession": "Engineer"}
items = person.items()
print(items)
print(type(items))
print()

# Iterating through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
