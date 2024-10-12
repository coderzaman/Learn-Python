# Local and Global Variables
# Local Variables: Defined within a function and accessible only inside that function.
# Global Variables: Defined outside of any function and accessible throughout the module.

# Example:

x = 10  # Global variable

def foo():
    y = 5  # Local variable
    print(f"Inside foo: x = {x}, y = {y}")

foo()
print(f"Outside foo: x = {x}")
# Output:
# Inside foo: x = 10, y = 5
# Outside foo: x = 10


# Note: Attempting to access a local variable outside its function raises a NameError.

def bar():
    z = 20

bar()
# print(z)  # Raises NameError: name 'z' is not defined

