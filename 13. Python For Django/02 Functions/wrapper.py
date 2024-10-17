# Higher Order Function -> Accepts function as argument or returns function

# Wrapper
def myWrapper(fn):
    def test():
        print("I am from test! Before")
        fn()
        print("I am from test! After")

    return test

# Decorators
@myWrapper
def greet():
    print("Hello world!")

@myWrapper
def hello():
    print("Hello Hello")


greet()
print()

hello()