# Example 1: Basic Function
# Task: Define a function that prints a welcome message.

def welcome():
    """Prints a welcome message."""
    print("Welcome to Python Functions!")

welcome()  # Output: Welcome to Python Functions!

# Example 2: Function with Multiple Parameters
# Task: Define a function that takes two numbers and returns their sum.

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

result = add(5, 7)
print(result)  # Output: 12


# Example 3: Using Default Parameters
# Task: Define a function that greets a user, with a default name of "Guest".
def greet(name="Guest"):
    """Greets the user by name."""
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!


# Example 4: Recursive Function
# Task: Define a recursive function to compute the factorial of a number.
def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120

# Exercise 1: Factorial Function
# Task: Write a function compute_factorial(n) that returns the factorial of n using recursion.
#
# Solution:
def compute_factorial(n):
    """Computes the factorial of n recursively."""
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * compute_factorial(n - 1)

# Testing the function
print(compute_factorial(5))  # Output: 120
print(compute_factorial(0))  # Output: 1
print(compute_factorial(-3)) # Output: Factorial not defined for negative numbers.


# Exercise 2: Fibonacci Sequence
# Task: Write a function fibonacci(n) that returns the nth Fibonacci number using recursion

def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n < 0:
        return "Fibonacci number not defined for negative indices."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the function
print(fibonacci(6))  # Output: 8
print(fibonacci(0))  # Output: 0
print(fibonacci(-2)) # Output: Fibonacci number not defined for negative indices.


# Exercise 3: Generator for Even Numbers
# Task: Write a generator function even_numbers(limit) that yields even numbers up to a specified limit.
def even_numbers(limit):
    for x in range(2, limit+1, 2):
        yield x

for even in even_numbers(10):
    print(even)