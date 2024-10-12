# Generators are a special type of function that return an iterator, allowing you to iterate over a sequence of values lazily
# (i.e., one at a time and only when needed). They are memory-efficient and suitable for handling large datasets

# Defining a Generator:
# Use the yield keyword instead of return to produce a value.

def countdown(n):
    while n > 0:
        yield  n
        n -= 1

for number in countdown(5):
    print(number)

# Example: Fibonacci Generator
def fibonacci_gen():
   a, b = 0, 1
   while True:
       yield a
       a,b = b, a + b


fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))
