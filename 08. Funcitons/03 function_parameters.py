# Positional Arguments
from orca.settings import profile


def add(a, b): # Here a and b is parameter
    return a + b

result = add(5, 3) #here 5, 3 is argument
print(result)  # Output: 8
print()


# Keyword Arguments
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(age=26, name="Abdullah")

print()

# Default Arguments
# Parameters that assume a default value if no argument is provided.

def greet(name = "guest"):
    print(f"Hello, {name}")

greet()
greet("Abdullah")

print()

# Variable-Length Arguments
# *args allows you to pass any number of positional arguments (i.e., arguments without a keyword) to a function. It collects these arguments into a tuple.

# Multiplication of numbers
def multi_array(*numbers):
    mul = 1
    for number in numbers:
        mul *= number
    return mul


result = multi_array(1,2,3,4,5)
print(result)
print()

# **kwargs: Keyword Variable-length Arguments
# **kwargs allows you to pass any number of keyword arguments (i.e., arguments with a key and a value, like key=value) to a function. It collects these arguments into a dictionary.

# Example:

def build_profile(first, last, **kwargs):
    profile = {"first_name": first, "last_name": last}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

profile = build_profile("Abdullah", "Abdur Rahman", location="Cox's Bazar, Bangladesh", occupation="Engineer", fav_color ="Black and White")
print(profile)