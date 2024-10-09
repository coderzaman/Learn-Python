name = "Alice"
age = 25

s = "My name is: {}, and age is: {}".format(name,age)
print(s)

# Specifying Order
s = "My name is: {0}, and age is: {1}. {0} Love python".format(name,age)
print(s)

# Specifying Keys:
s = "My name is: {name}, and age is: {age}. {name} Love python".format(name = name,age=age)
print(s)

# f-strings (Formatted String Literals)
# Introduced in Python 3.6, f-strings offer a more concise and readable way to embed expressions inside string literals.

print(f"My name is: {name}, and age is: {age}. {name} Love python")


a = 10
b = 20

print(f'Sum of {a} + {b} is: {a+b} ')

# Using Methods Inside f-strings:
name = "david"
s = f"My name is {name.capitalize()}."
print(s)  # Output: "My name is David."




