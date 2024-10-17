from functools import reduce

# reduce function work on an iterable and process items and generate a result

li = [1,2,3,4,5,6]

sum = reduce(lambda x,y: x+y, li)
print(sum)

sum = reduce(lambda x,y: x+y, li)
