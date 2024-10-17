# Lamda function

# function
# lambda argument:expression

add = lambda x,y : x + y
print(add(12,34))


# We can call and execute lamda function in single line also

add = ((lambda x,y : x + y)(6,5)) # This call IIFE(Immediately Invoked Function Expression)
print(add)