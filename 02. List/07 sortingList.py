# a. sort() Method
# Sorts the list in place, modifying the original list.
from audioop import reverse

# Syntax
# my_list.sort(reverse=False, key=None)


fruits = ["banana", "apple", "cherry", "date"]
fruits.sort()
print(fruits)

# Reverse List with slicing
print(fruits[::-1])


# Sorting in descending order
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort(reverse=True)
print(numbers)

# Sorting based on the length of strings
#ket length work on string
fruits.sort(key=len)
print(fruits)

# b. sorted() Function
# Returns a new sorted list without modifying the original list.
fruits = ["banana", "apple", "cherry", "date"]
sorted_fruits = sorted(fruits)
print(fruits)


#reverse order
rev_sorted_fruits = sorted(fruits, reverse=True)
print(rev_sorted_fruits)


# c. Sorting with Custom Keys
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
students.sort(key=lambda student:student[1])

# Sorting by age, then by name
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 25},
    {"name": "Dave", "age": 20}
]

# Sort first by age, then by name
people.sort(key=lambda person:(person["age"],person["name"]))
print(people)

# Sort first by name, then by age with sorted
sorted_with_multiple_key = sorted(people, key=lambda person:(person["name"],person["age"]))
