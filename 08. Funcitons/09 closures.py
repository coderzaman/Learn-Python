# A closure occurs when a nested function captures the local variables from its enclosing scope. Closures enable the creation of functions with preserved state.

# Example:

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

time_here = make_multiplier(3)
print(time_here(5))

times_five = make_multiplier(5)
print(times_five(5))

# Explanation:
# make_multiplier is a higher-order function that returns the multiplier function.
# The multiplier function retains access to the factor variable from its enclosing scope, even after make_multiplier has finished executing.
