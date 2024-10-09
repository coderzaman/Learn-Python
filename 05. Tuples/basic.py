# Empty tuple
empty_tuple = ()
print(empty_tuple)
print()

# Tuple with multiple elements
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')
print()

# Without Parentheses (Tuple Packing)
numbers = 1,2,3,4,5
print(numbers)
print(type(numbers))

# Using the tuple() Constructor
fruits = tuple(["apple", "banana", "cherry"])
print(fruits)


# From a string
letter = tuple("Python")
print(letter)

# Tuple Immutability
# Tuples are immutable, meaning that once a tuple is created, its elements cannot be changed, added, or removed.
s = (1, 2, 3)
# Attempting to modify an element
# s[0] = 10  # This will raise a TypeError

# Attempting to add an element
# s.append(4)  # AttributeError: 'tuple' object has no attribute 'append'

# Attempting to remove an element
# del s[1]  # TypeError: 'tuple' object doesn't support item deletion

# Tuple Indexing and Slicing
# Like lists, tuples support indexing and slicing to access their element
s = ("a", "b", "c", "d", "e")

# Indexing
print(s[0])   # Output: 'a'
print(s[-1])  # Output: 'e'

# Slicing
print(s[1:4])   # Output: ('b', 'c', 'd')
print(s[:3])    # Output: ('a', 'b', 'c')
print(s[2:])    # Output: ('c', 'd', 'e')
print(s[::2])   # Output: ('a', 'c', 'e')


# Tuple Concatenation and Repetition
# Tuples support concatenation using the + operator and repetition using the * operator.

t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
t3 = t1 + t2
print(t3)  # Output: (1, 2, 3, 4, 5)

# Repetition
t4 = ("repeat",) * 3
print(t4)  # Output: ('repeat', 'repeat', 'repeat')

# Important Note on Repetition(Single-Element Tuples):
# To create a single-element tuple, include a comma:
single = ("single",)
print(single)  # Output: ('single',)

not_a_tuple = ("single")
print(type(not_a_tuple))  # Output: 'single'



