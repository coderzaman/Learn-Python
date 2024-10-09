# Remove whitespace or specified characters from the beginning and/or end of a string.

s = "   Hello, World!   "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Removing Specific Characters:
s = "###Hello, World!###"
print(s.strip("#"))

