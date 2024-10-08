# Example 1: Determine Pass or Fail
score = 75

if score >= 60:
    print("Pass")
else:
    print("Fail")

# Example 2: Grading System
score = 88

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# Example 3: Nested if Statements
age = 22
has_license = True

if age >= 18:
    print("Eligible to drive.")
    if has_license:
        print("You can drive a car.")
    else:
        print("You need a driver's license to drive.")
else:
    print("Not eligible to drive.")

# Exercise 4: Even or Odd
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 5: Leap Year Checker
# Rules:
# A year is a leap year if it is divisible by 4 and not divisible by 100, unless it is also divisible by 400.

year = 2000

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



# Exercise 5: Maximum of Three Numbers
a = 10
b = 25
c = 20

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print(f"The maximum number is {max_num}.")
