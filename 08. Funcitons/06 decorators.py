# A decorator is a function that wraps another function to modify or extend its behavior, without changing the original
# function's code. Decorators allow you to "decorate" or add additional functionality to functions in a reusable way.

# How Your Code Works:
# Define the Decorator:
def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()  # This is where the original function (say_hello) is called
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()


# Example: Logging Decorator:
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments {args} and {kwargs}.")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(a, b):
    return a + b

result = add(5, 3)
# Output:
# Function 'add' was called with arguments (5, 3) and {}.
print(result)  # Output: 8
