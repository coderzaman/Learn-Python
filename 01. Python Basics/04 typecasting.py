# Implicit Typecasting
x = 10
y = 10.34

print(x+y) #automatic typecast to float


x = "hello"
y = 10

# print(x+y) # Uncommenting this line will raise TypeError

print(x * y)  # print hello to 10 times

# Explicit Typecasting
num = "100"
print(type(num))

num = int(num)
print(type(num))

num_str = "99.99"
num_float = float(num_str)
print(num_float)        # Output: 99.99
print(type(num_float))

invalid_str = "abc"
# num = int(invalid_str)  # Raises ValueError: invalid literal for int() with base 10: 'abc'

# Converting Numbers to Strings
# Integer to String
num_int = 50
num_str = str(num_int)
print(num_str)          # Output: "50"
print(type(num_str))    # Output: <class 'str'>

# Float to String
num_float = 3.1415
num_str = str(num_float)
print(num_str)          # Output: "3.1415"
print(type(num_str))    # Output: <class 'str'>

# Converting Lists to Tuples and Sets
my_list = [10,30,32,45,10]
my_tuple = tuple(my_list)
print(type(my_tuple))

my_set = set(my_list)
print(my_set)

# Converting Tuples to Lists
my_tuple = (10,20,30)
my_list = list(my_tuple)
my_list.append(340)
print(my_list)


# Converting Key-Value Pairs to Dictionary
# List of Tuples to Dictionary
pairs = [("a",1), ("b",2), (3,3)]
my_dict = dict(pairs)
print(my_dict)

# Typecasting with Complex Data Structures
# Typecasting with Complex Data Structures
str_list = ["1", "2", "3", "4"]
int_list = [int(item) for item in str_list]
print(int_list)


# Flattening Nested Lists
nested_list = [[1,2],[3,4],[5,6]]
str_list = [str(item) for arrayItem in nested_list for item in arrayItem]
print(str_list)

# Converting Between Lists and Dictionaries
keys = ["name", "age", "city"]
values = ["Bob", 25, "New York"]

my_dict = dict(zip(keys,values))
print(my_dict)