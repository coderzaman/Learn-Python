# Logical Operators
# and: Both conditions must be True.
# or: At least one condition must be True.
# not: Inverts the truth value of the condition.
#
# Examples
# a. Using and
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive a car.")

# b. Using or
is_weekend = True
has_free_time = False

if is_weekend or has_free_time:
    print("You can go out.")

# c. Using not
is_raining = False

if not is_raining:
    print("You don't need an umbrella.")
