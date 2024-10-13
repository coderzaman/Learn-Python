# a. Chained Comparisons
# Python allows you to chain multiple comparisons in a single statement, making the code more concise and readable.

age = 25

if 18 <= age < 30:
    print("Young adult")

age = 31

if 18 <= age < 30:
    print("Young adult")

# Using Functions in Conditions
def is_adult(age):
    return age >= 18

age = 20

if is_adult(age):
    print("You are an adult.")

 # Short-Circuit Evaluation
# Logical operators in Python use short-circuit evaluation, meaning the second condition is evaluated only if necessary.

def check_condition():
    print("Checking condition...")
    return True

if False and check_condition():
    print("This won't print.")
