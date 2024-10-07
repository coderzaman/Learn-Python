# 1. Equal to (==)
a = 5
b = 5
c = 10

print(a == b)  # Output: True
print(a == c)  # Output: False


# 2. Not Equal to (!=)
x = "Python"
y = "Java"
z = "Python"

print(x != y)  # Output: True
print(x != z)  # Output: False

# 3. Greater Than (>)
num1 = 15
num2 = 10

print(num1 > num2)  # Output: True
print(num2 > num1)  # Output: False

# 4. Less Than (<)
a = 3
b = 7

print(a < b)  # Output: True
print(b < a)  # Output: False


# 5. Greater Than or Equal to (>=)
x = 20
y = 20
z = 15

print(x >= y)  # Output: True
print(z >= y)  # Output: False

# 6. Less Than or Equal to (<=
m = 8
n = 12
p = 8

print(m <= n)  # Output: True
print(m <= p)  # Output: True
print(n <= m)  # Output: False

# 7. Identity Operators (is, is not)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # Output: True
print(a is c)      # Output: False
print(a is not c)  # Output: True
print(a is not b)

# 8. Membership Operators (in, not in)
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)     # Output: True
print("grape" in fruits)      # Output: False
print("grape" not in fruits)  # Output: True

# 9. Operator Precedence
result = 3 + 4 > 5  # Evaluated as (3 + 4) > 5
print(result)        # Output: True

result = 3 + (4 > 5)  # Evaluated as 3 + False => 3 + 0 => 3
print(result)        # Output: 3

# 10 Chaining Comparison Operators
x = 5
print(1 < x < 10)  # Output: True
print(5 < x < 10)  # Output: False


# is and is not concept exercise
a = [1, 2, 3]
b = a
c = [1, 2, 3]

a = 10
b = 10
print(id(a), id(b))
print(a is b)

c = a

print(a is c)
print(b is  c)
print(c is a)

a = "Hello world"
b = "Hello world"

print(a is b)




