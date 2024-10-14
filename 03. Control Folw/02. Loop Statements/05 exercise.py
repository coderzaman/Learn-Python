# Exercise 1: Multiplication Table
# Task: Write a program that prints the multiplication table for numbers 1 through 5.
import math

for i in range(1,6):
    for j in range(1,11):
        print(f'{i} * {j} = {i*j}')
    print()

# Exercise 2: Prime Number Checker
# Task: Write a program that checks if a given number is a prime number.

user_input = int(input("Enter a Number Check Prime or Not: "))

if user_input < 2:
    print(f'{user_input} is not a prime number')
else:
    for i in range(2,  int(math.floor(user_input**0.5)) +1):
        if user_input % 2 == 0:
            print(f'{user_input} is a prime number')
            break
    else:
        print(f'{user_input} is a prime number')


# Exercise 3: FizzBuzz
# Task: For numbers from 1 to 15, print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.

for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 4: Factorial Calculator
# Task: Calculate the factorial of a given number.

userInput = int(input("Please enter number: "))

factor = 1

if userInput < 0:
    print("Not Possible for this Number")
elif userInput <=1:
    print(f'Factorial of {userInput} is 1')
else:
    for x in range(2, userInput+1):
        factor *= x
    print(f'Factorial of {userInput} is {factor}')

