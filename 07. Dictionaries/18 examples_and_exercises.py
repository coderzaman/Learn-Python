# Example 1: Storing and Retrieving User Information
# Creating a dictionary to store user information
from itertools import product

user = {
    "username": "alice123",
    "email": "alice@example.com",
    "age": 30,
    "is_active": True
}

# Accessing values
print(user["username"])  # Output: alice123
print(user.get("email")) # Output: alice@example.com

# Adding a new key-value pair
user["profession"] = "Engineer"

# Updating an existing key
user["age"] = 31

# Removing a key-value pair
user.pop("is_active")

print(user)
# Output: {'username': 'alice123', 'email': 'alice@example.com', 'age': 31, 'profession': 'Engineer'}


print()

# Example 2: Counting Occurrences Using Dictionaries
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

# Using defaultdict for simplification
from collections import defaultdict

word_counts = defaultdict(int)
for word in words:
    word_counts[word] += 1

print(word_counts)

print()

# Example 3: Merging Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged = {**dict1, **dict2}
print(merged)

# Example 4: Nested Dictionaries
# Nested dictionary representing students and their grades
students = {
    "Alice": {"math": 90, "science": 85},
    "Bob": {"math": 75, "science": 95},
    "Charlie": {"math": 85, "science": 80}
}

# Accessing nested values
print(students["Alice"]["math"])

# Adding a new subject for Bob
students["Bob"]["english"] = 88

print(students)



# Exercise 1: Creating and Accessing a Dictionary
# Task: Create a dictionary to store information about a book, including its title, author, publication year, and genres. Then, access and print the author's name
# Creating the dictionary
book = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publication_year": 1960,
    "genres": ["Fiction", "Classic", "Coming-of-age"]
}

# Accessing the author's name
author = book["author"]
print(author)  # Output: Harper Lee

print()

# Exercise 2: Updating and Removing Dictionary Entries
# Task: Given the following dictionary representing a movie, update its rating to 8.5 and remove the director from the dictionary.

# movie = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "year": 2010,
#     "rating": 8.0
# }

# Expected Output:
# {
#     "title": "Inception",
#     "year": 2010,
#     "rating": 8.5
# }

# Solution:
movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "rating": 8.0
}

# Updating the rating
movie["rating"] = 8.5

# Removing the director
movie.pop("director")

print(movie)
# Output: {'title': 'Inception', 'year': 2010, 'rating': 8.5}

# Exercise 3: Using .get() with Default Values
# Task: Given a dictionary representing a car, retrieve the value of the key "color". If the key does not exist, return "Unknown".

# car = {
#     "make": "Toyota",
#     "model": "Camry",
#     "year": 2020
# }

# Expected Output:
# Unknown

# Solution:
# car = {
#     "make": "Toyota",
#     "model": "Camry",
#     "year": 2020
# }
#
# color = car.get("color", "Unknown")
# print(color)  # Output: Unknown

# Exercise 4: Iterating Through a Dictionary
# Task: Given a dictionary of students and their scores, print each student's name along with their score.
#

# students_scores = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 90
# }

# Expected Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: 90
#

# Solution:
students_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

for student, score in students_scores.items():
    print(f"{student}: {score}")

print()

# Exercise 5: Merging Multiple Dictionaries
# Task: Given a list of dictionaries representing various products, merge them into a single dictionary. If there are duplicate keys, later entries should overwrite earlier ones.

# products = [
#     {"id": 1, "name": "Laptop", "price": 999},
#     {"id": 2, "name": "Smartphone", "price": 499},
#     {"id": 1, "name": "Gaming Laptop", "price": 1299}
# ]

# Expected Output:
# {
#     1: {"id": 1, "name": "Gaming Laptop", "price": 1299},
#     2: {"id": 2, "name": "Smartphone", "price": 499}
# }

# Solution:

# Assuming that the "id" is the unique key.
products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Smartphone", "price": 499},
    {"id": 1, "name": "Gaming Laptop", "price": 1299}
]

newDict = {}

for product in products:
    newDict.update({
        product["id"]: product
    })

print(newDict)

# or

newDict = {}

for product in products:
   newDict[product["id"]] = product

print(newDict)