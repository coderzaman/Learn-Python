# 1. and Operator
# Example 1: Both conditions True

age = 25
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # Output: True

# Example 2: One condition False
age = 16
has_license = False

can_drive = age >= 18 and has_license
print(can_drive)  # Output: False

# Example 3: Mixed conditions
age = 20
has_license = False

can_drive = age >= 18 and has_license
print(can_drive)  # Output: False

# 2. or Operator
# Example 1: Both conditions True
is_weekend = True
is_holiday = True

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # Output: True

# Example 2: One condition True
is_weekend = True
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # Output: True

# Example 3: Both conditions False
is_weekend = False
is_holiday = False

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # Output: False

# 3. not Operator
# Example 1: Negating True
is_sunny = True
is_not_sunny = not is_sunny
print(is_not_sunny)  # Output: False

# Example 2: Negating False
is_raining = False
is_not_raining = not is_raining
print(is_not_raining)  # Output: True

# Example 3: Using with conditions
age = 20
has_license = False

can_drive = age >= 18 and has_license
print(can_drive)  # Output: False

can_not_drive = not can_drive
print(can_not_drive)  # Output: True


# 4. Operator Precedence
# Precedence Hierarchy (Relevant to Logical Operators):
#
# Parentheses ()
# Unary not not
# Logical and and
# Logical or or

# Without parentheses
result = True or False and False
print(result)  # Output: True

# With parentheses to change precedence
result = (True or False) and False
print(result)  # Output: False

# 5. Short-Circuit Evaluation
def first():
    print("First function called")
    return False

def second():
    print("Second function called")
    return True

result = first() and second()
print(result)

# Output:
# First function called
# False

# 5. Short-Circuit Evaluation

# a. and Operator:
# Behavior:
# If the first operand is False, Python does not evaluate the second
# operand because the overall result cannot be True.

# Example:
def first():
    print("First function called")
    return False

def second():
    print("Second function called")
    return True

result = first() and second()
print(result)

# Output:
# First function called
# False

# b. or Operator:
# Behavior:
# If the first operand is True, Python does not evaluate the second operand because the overall result is already True.
# Example:
def first():
    print("First function called")
    return True

def second():
    print("Second function called")
    return False

result = first() or second()
print(result)

# Output:
# First function called
# True

# 6. Truthy and Falsy Values
# Falsy Values
print(bool(False))    # Output: False
print(bool(None))     # Output: False
print(bool(0))        # Output: False
print(bool(""))       # Output: False
print(bool([]))       # Output: False

# Truthy Values
print(bool(True))     # Output: True
print(bool(1))        # Output: True
print(bool("Hello"))  # Output: True
print(bool([1, 2]))   # Output: True
print(bool({'a': 1})) # Output: True

# 7. Using Logical Operators in Control Flow
# a. Using and in if Statements
age = 22
has_license = True

if age >= 18 and has_license:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

# b. Using or in if Statements
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax today!")
else:
    print("Time to work!")

# c. Using not in if Statements
is_raining = False

if not is_raining:
    print("You don't need an umbrella today.")
else:
    print("Don't forget your umbrella!")

# d. Combining Multiple Logical Operators
age = 30
has_license = True
is_insured = False

if (age >= 18 and has_license) or is_insured:
    print("Eligible for the driving test.")
else:
    print("Not eligible for the driving test.")

# 9. Advanced Topics
# a. Combining Logical Operators with Other Operators
# Logical operators can be combined with comparison operators, membership operators, and more to form complex conditions.

# Example:
username = "admin"
password = "password123"

if username == "admin" and password == "password123":
    print("Access granted.")
else:
    print("Access denied.")
# b. Logical Operators in List Comprehensions
numbers = range(1, 21)
filtered = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
print(filtered)  # Output: [6, 12, 18]

# c. Using Logical Operators with Functions
def is_even(num):
    return num % 2 == 0

def is_positive(num):
    return num > 0

number = 4

if is_even(number) and is_positive(number):
    print("Number is positive and even.")
else:
    print("Number does not meet the criteria.")

# d. Ternary Conditional Operator with Logical Operators
age = 20
has_permission = True

status = "Allowed" if age >= 18 and has_permission else "Not Allowed"
