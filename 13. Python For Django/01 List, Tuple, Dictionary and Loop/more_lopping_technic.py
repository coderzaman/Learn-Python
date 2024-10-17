# We can fetch index and item of a tuple and list

# enumerate
myTuple = ("Bangladesh", "Pakistan", "Afghanistan", ("India", "Israel"))

for index, value in enumerate(myTuple):
    print(index, value)

print()
myList = ["Bangladesh", "Pakistan", "Afghanistan", ("India", "Israel")]
for index, value in enumerate(myList):
    print(index, value)
print()
# we can iterate 2 or more list or tuple parallel with zip function(But need has same length)

myTuple = (1, 2, 2)
myList = ["Bangladesh", "Pakistan", "Afghanistan"]

for x,y in zip(myTuple, myList):
    print(x,y)

print()

for x, y in zip(myList, myTuple):
    print(x, y)

# Sort array through function with sorted function
print()
for c in sorted(myList):
    print(c)

print()
# for reverse
for c in sorted(myList, reverse=True):
    print(c)
print()
# We can apply it with set or tuple
my_set = {1,2,3,4,9,2,8,4,5,3,5,7}

for x in sorted(my_set):
    print(x)