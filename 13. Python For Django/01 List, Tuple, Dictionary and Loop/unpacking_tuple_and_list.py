myTuple = ("Bangladesh", "Pakistan", "Afghanistan")

#unpacking
c1, c2, c3 = myTuple

print(c1, c2, c3)

# No variable assign the left must be equal to no of tuple item
# c1, c2, c3, c4 = myTuple #ValueError
# c1, c2 = myTuple #ValueError

myList = ["Bangladesh", "Pakistan", "Afghanistan"]
c1, c2, c3 = myList
print(c1, c2, c3)

# unpacking nested element in variable
myTuple = ("Bangladesh", "Pakistan", "Afghanistan", ("India", "Israel"))
c1, c2, c3, [c4, c5] = myTuple
print(c1, c2, c3, c4, c5)

# or use
c1, c2, c3, (c4, c5) = myTuple
print(c1, c2, c3, c4, c5)

# Also similar for list
myList = ["Bangladesh", "Pakistan", "Afghanistan",  ("India", "Israel")]
c1, c2, c3, (c4, c5) = myList
print(c1, c2, c3, c4, c5)

myList = ["Bangladesh", "Pakistan", "Afghanistan",  ["India", "Israel"]]
c1, c2, c3, (c4, c5) = myList
print(c1, c2, c3, c4, c5)

myList = ["Bangladesh", "Pakistan", "Afghanistan",  ["India", "Israel"]]
c1, c2, c3, [c4, c5] = myList
print(c1, c2, c3, c4, c5)

# We can use () [] for list or tuple unpacking

# multiple variable assignment
a, b = 10, "Aktaruzzaman"
print(a,b)

# We can use * FOR multiple value unpacking from list or tuple. It *var return a list

a, b, *c = ["Bangladesh", "Pakistan", "Afghanistan",  ["India", "Israel"]]
print(a, b, c)


a, b, *c = ["Bangladesh", "Pakistan", "Afghanistan",  "India", "Israel"]
print(a, b, c)

a, *b, c = ["Bangladesh", "Pakistan", "Afghanistan",  "India", "Israel"]
print(a, b, c)

*a, b, c = ["Bangladesh", "Pakistan", "Afghanistan",  "India", "Israel"]
print(a, b, c)

# But we can not use double * variable in a single statement
# a, *b, *c = ["Bangladesh", "Pakistan", "Afghanistan",  ["India", "Israel"]] #SyntaxError


