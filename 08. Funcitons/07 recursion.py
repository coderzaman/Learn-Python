# Recursion is a programming technique where a function calls itself to solve smaller instances of a problem. It is particularly useful for tasks that can be divided into similar subtasks.
#
# Key Components of Recursion:
#
# Base Case: The condition under which the recursion stops.
# Recursive Case: The part of the function where it calls itself with modified parameters.

# Example: Factorial Function
def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120

"""
How it work:

Note:
{} => indicate return value
[] => function call


[factorial(5)]
{5 * [factorial(4)]} 
5 * {4* [factorial(3)]} 
20 * {3 * [factorial(2)]} 
60 * {2 * [factorial(1)]} 
120 * {1 * [factorial(0)]} 
120 * 1
"""

# Example: Fibonacci Sequence
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0  # Base case
    elif n == 1:
        return 1  # Base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case

print(fibonacci(6))  # Output: 8

"""
How It work:


Note:
{} => indicate return value
[] => function call


fibonacci(6)
{[fibonacci(5)] + fibonacci(4)}
{[fibonacci(4)] + fibonacci(3)} + fibonacci(4)
{[fibonacci(3)] + fibonacci(2)} + fibonacci(3) + fibonacci(4)
{[fibonacci(2)] + fibonacci(1)} fibonacci(2) + fibonacci(3) + fibonacci(4)
{[fibonacci(1)] + fibonacci(0)} + fibonacci(1) + fibonacci(2) + fibonacci(3) + fibonacci(4)

{1} + [fibonacci(0)}] + fibonacci(1) + fibonacci(2) + fibonacci(3) + fibonacci(4)
1 + {0} + [fibonacci(1)]+ fibonacci(2) + fibonacci(3) + fibonacci(4)
1 + {1} + [fibonacci(2)] + fibonacci(3) + fibonacci(4)
2 + {[fibonacci(1)] + fibonacci(0)} + fibonacci(3) + fibonacci(4)
2 + {1} + [fibonacci(0)] + fibonacci(3) + fibonacci(4)
3 + {0} + [fibonacci(3)] + fibonacci(4)
3 + {[fibonacci(2)] + fibonacci(1)} +  fibonacci(4)
3 + {[fibonacci(1)] + fibonacci(0)} + fibonacci(1)} +  fibonacci(4)
3 + {1} + [fibonacci(0)] + fibonacci(1)} +  fibonacci(4)
4 + {0} + [fibonacci(1)] +  fibonacci(4)
4 + {1} + [fibonacci(4)]
5 + {[fibonacci(3)] + fibonacci(2)}
5 + {[fibonacci(2)] + fibonacci(1)} + fibonacci(2)
5 + {[fibonacci(1)] + fibonacci(0)} + fibonacci(1) + fibonacci(2)
5 + {1} +  [fibonacci(0)] + fibonacci(1) + fibonacci(2)
6 + {0} + [fibonacci(1)] + fibonacci(2)
6 + {1} + [fibonacci(2)]
7 + {[fibonacci(1)] + fibonacci(0)}
7 + {1} + [fibonacci(0)]
8 + [fibonacci(0)]
8 + {0}
8
"""

