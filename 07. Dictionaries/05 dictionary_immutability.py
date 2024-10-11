# While the dictionary structure is mutable, meaning you can add, remove, or change key-value pairs, the keys themselves must be immutable (hashable).
# However, the values can be of any type, including mutable ones like lists or other dictionaries.

# Dictionary with mutable values
data = {
    "fruits": ["apple", "banana"],
    "numbers": [1, 2, 3],
    "details": {"name": "Alice", "age": 30}
}

# Modifying a mutable value
data["fruits"].append("cherry")
print(data["fruits"])  # Output: ['apple', 'banana', 'cherry']

# Immutable Keys:
# Valid keys (immutable)
valid_dict = {
    "name": "Alice",
    1: "one",
    (2, 3): "tuple key"
}

# Invalid keys (mutable)
# invalid_dict = {
#     ["list"]: "invalid"  # Raises TypeError: unhashable type: 'list'
# }

