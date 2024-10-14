# Strings can be created in various ways:
# Using single quotes

string1 = 'Hello, World! '

# Using double quotes
string2 = "Hello, World!"

# Using triple quotes for multi-line strings
string3 = """Hello,
World! 
"""

#Converting number to string. Number can be integer or float
string4 = str(12.3)

print(string1)
print(string2)
print(string3)
print(string4)


# String Immutability
s = "Hello"
# Attempting to change the first character
# s[0] = 'h'  # This will raise a TypeError

# Correct way: Create a new string
s_new = 'h' + s[1:]
print(s_new)  # Output: "hello"

# String Indexing and Slicing
s = "Python"

# Positive indices
print(s[0])  # Output: 'P'
print(s[2])  # Output: 't'

# Negative indices
print(s[-1])  # Output: 'n'
print(s[-3])  # Output: 'h'

# Slicing
print(s[1:4])   # Output: 'yth'
print(s[:3])    # Output: 'Pyt'
print(s[3:])    # Output: 'hon'
print(s[-4:-1]) # Output: 'tho'

# Concatenation
# Concatenation
s1 = "Hello"
s2 = "World"
s3 = s1 + ", " + s2 + "!"
print(s3)  # Output: "Hello, World!"

# Repetition
s4 = "Echo! " * 3
print(s4)  # Output: "Echo! Echo! Echo! "
