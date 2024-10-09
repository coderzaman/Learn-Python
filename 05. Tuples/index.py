# Returns the index of the first occurrence of a specified value. Raises a ValueError if the value is not found.
t = ("apple", "banana", "cherry", "banana")

index_banana = t.index("banana")
print(index_banana)  # Output: 1

# Finding index with start and end parameters
index_banana_second = t.index("banana", 2)
print(index_banana_second)  # Output: 3

# Value not in tuple
# t.index("orange")  # Raises ValueError: tuple.index(x): x not in tuple

# Handling ValueError:
t = (1, 2, 3)
try:
    t.index(4)
except ValueError:
    print("Value not found in tuple.")  # Output: Value not found in tuple.
