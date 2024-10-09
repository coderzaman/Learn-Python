# Exercise 1: Filter and Transform
# Task: Given a list of numbers, create a new list containing the cubes of numbers that are divisible by 3.
import time

numbers = [1, 3, 4, 6, 7, 9, 12]
cube_div3 = [number**3 for number in numbers if number % 3 == 0]
print(cube_div3)

# Create a Dictionary from Two Lists
# Exercise 2: Create a Dictionary from Two Lists

names = ["Alice", "Bob", "Charlie"]
ages = [25, 22, 23]

# join_list = zip(names,ages)
#
# for x in join_list:
#     print(x[0],x[1])

makeDict = {name: age for name, age in zip(names,ages)}
print()

print(makeDict)

# Exercise 3: Prime Number Generator
# Task: Create a generator expression that yields prime numbers up to 50.

# Solution
# Creating a generator expression for prime numbers is more complex because it involves checking each number for primality. Instead, we'll use a generator function with yield.


def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(number**0.5)+1):
           if number % i == 0:
               return False
        return True

primeNumber1_50 = [number for number in range(1,51) if is_prime(number)]
print(primeNumber1_50)

# List Comprehension vs Loop
start_time = time.time()
square_list = [x** 2 for x in range(1,10000001)]
# print(square_list)
end_time = time.time()
print(f"List Comprehension took {end_time - start_time:.4f} seconds.")

# Using For Loop
start_time = time.time()
squares_loop = []

for x in range(1,10000001):
    squares_loop.append(squares_loop.append(x**2))
end_time = time.time()
print(f"For Loop took {end_time - start_time:.4f} seconds.")