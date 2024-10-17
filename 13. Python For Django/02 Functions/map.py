# map function
def func(n):
    return n*n*n

l = [3, 4, 1, 0, 6]
# map(function, iterable) return map iterator object
newIterable = map(func, l)

for i in newIterable:
    print(i)

# print(newIterable.__next__())[cause it is a iterator]
# we can convert iterator to list, tuple, set, or dictionary
print()
# we can also solve with it lambda
newIterable = list(map(lambda x: x**3, l))
print(newIterable)

newIterable = dict(map(lambda x: (x, x**3), l))
print(newIterable)


print()
listArr =  ["Apple", "Banana", "Cherry"]
flat_array = list(map(list, listArr))
print(flat_array)