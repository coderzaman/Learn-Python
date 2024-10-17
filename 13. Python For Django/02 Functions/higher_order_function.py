# A higher-order function is one that takes other functions as arguments or returns a function as its result.

# Simple Higher order Function
def hof(func):
    func()

def greeting():
    print("Hello")

hof(greeting)

# Implement a fileter function

myList = [1,2,4,5,6,7,8,9,10]

def my_filter(func, my_list):
    return [i for i in my_list if func(i)]

def my_map(func, my_list):
   return [func(i) for i in my_list]

even_list = my_filter(lambda x:x%2 == 0, myList)
print(even_list)

#Separtor
print()

odd_list = my_filter(lambda x:x%2 != 0, myList)
print(odd_list)

myList = ["apple", "banana", "chery", "date"]

upper_list = my_map(lambda x: x.upper(), myList)
print(upper_list)
print()


lower_list = my_map(lambda x: x.lower(), upper_list)
print(lower_list)

