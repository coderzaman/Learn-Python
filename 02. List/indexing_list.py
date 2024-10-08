# a. Positive Indexing
# Starts from 0 (first element) to n-1 (last element).
colors = ["red", "green", "blue", "yellow", "purple"]

print(colors[0])  # Output: red
print(colors[2])  # Output: blue
print(colors[4])  # Output: purple

# b. Negative Indexing
colors = ["red", "green", "blue", "yellow", "purple"]

print(colors[-1])  # Output: purple
print(colors[-3])  # Output: blue
print(colors[-5])  # Output: red


# Accessing Elements in Nested Lists
nested_list = [
    [1, 2, 3],
    ["a", "b", "c"],
    [True, False]
]

# print c
print(nested_list[1][2])

nested_list = [
    [1, 2, 3],
    ["a", "b", ["c","d",{"e": "egg", "f":"fog"},["g","h"]]],
    [True, False]
]

# print egg and g and h
print(nested_list[1][2][2]["e"])
print(nested_list[1][2][3][0])
print(nested_list[1][2][3][1])