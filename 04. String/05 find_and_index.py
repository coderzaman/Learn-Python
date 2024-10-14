# .find() and .index()
# .find() and .index() are used to locate the position of a substring within a string. Both return the lowest index where the substring is found.
#
# .find() returns -1 if the substring is not found.
# .index() raises a ValueError if the substring is not found.

s = "Hello, World!"
print(s.find("l"))

s = "Hello, World!"

# Using find()
position = s.find("World")
print(position)  # Output: 7

# Using index()
position = s.index("World")
print(position)  # Output: 7

# Substring not found
print(s.find("Python"))  # Output: -1
# print(s.index("Python"))  # Raises ValueError
