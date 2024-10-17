
# Lopping through nested tuple and list where nested item has equal numbers item

myTuple = (("a",1), ("b",2), ("c", 3), ("d", 4))

for x in myTuple:
    print(x) # Here x is a tuple
print()
# If apply unpacking technic
for x,y in myTuple:
    print(x,y)

# myTuple = (("a",1), ("b",2), ("c", 3), ("d", 4,4))

# for x,y in myTuple: #ValueError: Cause of nested tuple has not equal number of item
    # print(x,y)

print()
myTuple = (("a",1,1), ("b",2,2), ("c", 3,3), ("d", 4,4))

for x,y,z in myTuple:
    print(x,y,z)

print()



# We can also apply same operation for list
myList = [("a",1,1), ["b",2,2], ["c", 3,3], ["d", 4,4]]

for x,y,z in myList:
    print(x, y, z)