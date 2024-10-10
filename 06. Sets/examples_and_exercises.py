# Example 1: Removing Duplicates from a List
# Task: Given a list with duplicate elements, remove the duplicates using a set.
fruits = ["apple", "banana", "cherry", "apple", "banana", "date"]
unique_fruits = set(fruits)
print(unique_fruits)  # Output: {'banana', 'date', 'cherry', 'apple'}

# Example 2: Membership Testing
# Task: Check if a specific element exists in a set.
s = {"apple", "banana", "cherry"}
print("banana" in s)  # Output: True
print("grape" in s)   # Output: False


# Example 3: Set Operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# Union
print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(s1 & s2)  # Output: {3, 4}

# Difference
print(s1 - s2)  # Output: {1, 2}
print(s2 - s1)  # Output: {5, 6}

# Symmetric Difference
print(s1 ^ s2)  # Output: {1, 2, 5, 6}


# Exercise 1: Finding Common Elements
# Task: Given two lists, find the common elements using sets.
print()
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


print(set(list1) & set(list2))
print(set(list1).intersection(list2))

# Exercise 2: Counting Unique Words
# Task: Given a sentence, count the number of unique words using sets.
#
# Sentence: "Python is great and Python is fun"
#
# Expected Output: {'Python', 'is', 'great', 'and', 'fun'}

user_str = "Python is great and Python is fun"

str_word = user_str.split()

set_unique_word = set(str_word)
print(set_unique_word)

# Exercise 4: Checking for Anagrams
# Task: Write a function to check if two strings are anagrams using sets.
#
# Example:
#
# "listen" and "silent" → True
# "hello" and "world" → False

def are_anagrams_set(str1, str2):
    return sorted(set(str1)) == sorted(set(str2))

print(are_anagrams_set("listen", "silent"))  # Output: True
print(are_anagrams_set("hello", "world"))

# Exercise 5: Removing Specific Elements
# Task: Given a set of numbers, remove all even numbers.

# Set: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Expected Output: {1, 3, 5, 7, 9}
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
output_set = {number for number in numbers if number%2 != 0}
print(output_set)