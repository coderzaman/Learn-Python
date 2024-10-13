# Example 1: Basic String Manipulation
s = "  Python Programming  "

# Remove leading and trailing whitespace
s_clean = s.strip()
print(s_clean)  # Output: "Python Programming"

# Convert to uppercase
s_upper = s_clean.upper()
print(s_upper)  # Output: "PYTHON PROGRAMMING"

# Replace "Programming" with "Language"
s_replaced = s_clean.replace("Programming", "Language")
print(s_replaced)  # Output: "Python Language"

# Split into words
words = s_clean.split()
print(words)  # Output: ['Python', 'Programming']

# Join words with a hyphen
s_joined = '-'.join(words)
print(s_joined)  # Output: "Python-Programming"


# Example 2: Using .format() and f-strings
name = "Diana"
age = 27

# Using .format()
s1 = "My name is {} and I am {} years old.".format(name, age)
print(s1)  # Output: "My name is Diana and I am 27 years old."

# Using f-strings
s2 = f"My name is {name} and I am {age} years old."
print(s2)  # Output: "My name is Diana and I am 27 years old."

# Including expressions in f-strings
s3 = f"In five years, I will be {age + 5} years old."
print(s3)  # Output: "In five years, I will be 32 years old."


# Example 3: Checking String Content
s = "Hello123"

# Check if all characters are alphanumeric
print(s.isalnum())  # Output: True

# Check if all characters are alphabetic
print(s.isalpha())  # Output: False

# Check if all characters are digits
print(s.isdigit())  # Output: False

# Check if string starts with "He"
print(s.startswith("He"))  # Output: True

# Check if string ends with "123"
print(s.endswith("123"))  # Output: True


# Exercise 1: Palindrome Checker
# Task: Write a program that checks if a given string is a palindrome (reads the same backward as forward).

# str = "madam"
# print(str == str[::-1])


def is_palindrome(str_item):
    str_item = ''.join(str_item.split(" ")).lower()
    return str_item == str_item[::-1]



str_list =  ["Racecar", "Hello", "A man a plan a canal Panama", "Python"]

for item in str_list:
    if is_palindrome(item):
        print(f'{item} is Palindrome')
    else:
        print(f'{item} is not Palindrome')

# Exercise 2: Sentence Capitalization
sentence = "python programming is fun!"
capitalized = sentence.title()
print(capitalized)

words = sentence.split()
capitalized_word = [word.capitalize() for word in words]
capitalized = ' '.join(capitalized_word)

print(capitalized)

# Exercise 3: Extracting Vowels
# Task: Extract all vowels from a given string and return them as a list.

# Solution:

s = "Hello World"

extract_vowel = [ch for ch in s if ch in "aeiouAeiou"]
print(extract_vowel)
set_list = set(extract_vowel)

print(' '.join(set_list))

