# .startswith() and .endswith()
# Check if a string starts or ends with a specified substring.
s = "Hello, World!"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World!"))   # Output: True
print(s.startswith("World"))  # Output: False

# Case Sensitivity:
# These methods are case-sensitive.
print(s.startswith("hello"))  # Output: False
