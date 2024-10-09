# replace()
# Replace occurrences of a substring with another substring.
s = "Hello, World!"
s_new = s.replace("World", "Python")
print(s_new)  # Output: "Hello, Python!"


# Limiting Replacements:
# The .replace() method can take an optional third argument specifying the maximum number of replacements.

s = "World, World,World!"
s_new = s.replace("World", "Earth", 2)
print(s_new)

# Replacing Multiple Occurrences:
s = "banana"
s_new = s.replace("a", "o")
print(s_new)



