# Default Dictionaries: The defaultdict class from the collections module provides dictionaries with default values for non-existent keys,
# avoiding the need to check for key existence.

# Advantages:
# Automatically initializes missing keys with a default value.
# Simplifies code by eliminating the need for key existence checks.

# Creating a defaultdict:

from collections import defaultdict


# Default value of int (0)
counts = defaultdict(int)

counts["apple"] += 1 # value is 0 + 1 = 1,
counts["orange"] += 2

print(counts)

# Default value of list
fruits = defaultdict(list)
print(fruits)

fruits["fruits"].append("Apple")
fruits["fruits"].append("Ornage")

print(fruits)

# Common Use Cases:
# Counting: Tallying occurrences of items.
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
words_counts = defaultdict(int)

for word in words:
    words_counts[word] += 1

print(words_counts)


# Grouping: Grouping items based on a key.
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "Diana", "grade": "C"},
    {"name": "Eve", "grade": "B"}
]

print()
grade_groups  = defaultdict(list)

for student in students:
    #Provide List name with student grade then append student name to list
    grade_groups[student["grade"]].append(student["name"])

print(grade_groups)

