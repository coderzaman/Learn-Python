# Return Values
# Functions can return values using the return statement. If no return statement is provided, the function returns None by default.

def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16

# Returning Multiple Values:
# Python functions can return multiple values as a tuple.

def get_coordinate():
    x = 10
    y = 14
    return x,y

coordinates = get_coordinate()
x_coordinate = coordinates[0]
y_coordinate = coordinates[1]

print(x_coordinate, y_coordinate)

x_coordinate, y_coordinate = coordinates
print(x_coordinate,y_coordinate)

