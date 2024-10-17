# Function
def hello(fname, lname):
    print(f"Full Name: {fname} {lname}")

# fname, lname -> parameter
# arguments -> Simanta, Paul (Passed Value)
# hello("Abu", "Huraira")

# Arbitrary Arguments
def fun1(*args):
    print(args[1])

#fun1("Abu", "Huraira", 25, True, False)

def hello2(fname, lname="Huraira"):
    print(f"Full Name: {fname} {lname}")


#hello2("Abu")


# Arbitrary Keyword Arguments
def fun2(**kwargs):
    print(kwargs['fname'])

#fun2(fname="Abu", lname="Huraira", age=25)

def hello3(*args, **kwargs):
    print(args, kwargs)

hello3()