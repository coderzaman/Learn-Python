l = [1, 3, 4, 6, 88, 4, 2, 9, 5]


#with list comprehension
even_number = [x for x in l if x%2==0]
print(even_number)
print()
#With function
def func(n):
    return n%2==0

even_number = [x for x in l if func(x)]
print(even_number)
print()

# fileter with function
even_number = list(filter(func, l))
print(even_number)
print()

# Lamda Function
even_number = list(filter(lambda x: x % 2 == 0, l))
print(even_number)