# Loop comprehension
# We can apply it to iterable -> List, Tuple, Dictionary, Set, Range, String

myList = [1, 2, 3, 4, 5, 6]

newList = [i+1 for i in myList]
print(myList, "\n")

newDict = {i: i*i for i in myList}
print(newDict, "\n")

newSet = {i**3 for i in myList}
print(newSet, "\n")

newTuple = tuple(i**4 for i in myList) #(comprehension) return a generator object, we convert it tuple
print(newSet, "\n")

# We can also assign tuple or list as comprehension item
newTlist = [(i, i**2, i**3) for i in newTuple]
print(newTlist, "\n")


myDict = {"one":1, "two": 2, "three":3, "four": 4}

newDict = {"key " + key: value for key,value in myDict.items()}
print(newDict, "\n")


# String
char_list = [x for x in "String"]
print(char_list, "\n")

# string => dictionary
char_dict = {x.upper(): x.lower() for x in "String"}
print(char_dict, "\n")


# Nested comprehension
# making matrix[
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# [0, 1, 2, 3]]

matrix = [[row for row in range(4)] for col in range(4)]
print(matrix)
print()
# transpose
transpose = [[matrix[row][col] for row in range(4)] for col in range(4)]
print(transpose)

print()
#platted list
flatted = [col for row in matrix for col in row ]
print(flatted)