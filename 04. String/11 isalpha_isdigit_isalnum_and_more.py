s1 = "HelloWorld"
print(s1.isalpha())  # Output: True  # All characters are alphabetic

s2 = "12345"
print(s2.isdigit())  # Output: True  # All characters are digits

s3 = "Hello123"
print(s3.isalnum())  # Output: True  # All characters are alphanumeric

s4 = "Hello World!"
print(s4.isalnum())  # Output: False  # Contains space and punctuation

# Other similar methods:
# .isspace(), .islower(), .isupper(), .istitle(), etc.

s5 = "   "
print(s5.isspace())  # Output: True

s6 = "hello"
print(s6.islower())  # Output: True

s7 = "HELLO"
print(s7.isupper())  # Output: True

s8 = "Hello"
print(s8.istitle())  # Output: True
