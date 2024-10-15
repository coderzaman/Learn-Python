# class A:
#     def __init__(self):
#         print("Class A")
#
# class B(A):
#     def __init__(self):
#         print("Class B")
#         A.__init__(self)
# class C(B):
#     def __init__(self):
#         print("Class C")
#         B.__init__(self)
#
# class D(C,B):
#     def __init__(self):
#         print("Class D")
#         C.__init__(self)
#         B.__init__(self)
#
#
# class E(D,C):
#     def __init__(self):
#         print("Class D")
#         D.__init__(self)
#         C.__init__(self)
# d = E()

# Diamond problem occurs here we see D, C, B. and A are called multiple time. So solve this problem we can use super() mehtod

# class A:
#     def __init__(self):
#         print("A")
#
# class B(A):
#     def __init__(self):
#         print("B")
#         super().__init__()
#
# class C(B):
#     def __init__(self):
#         print("C")
#         super().__init__()
#
# class D(B, C):
#     def __init__(self):
#         print("D")
#         super().__init__()
#
# d = D()
# print(D.__mro__)

# Cause of Error
# First Call to D.__init__():
#
# When you create an instance of D, the constructor of D is called first. This is correct.
# Call to super().__init__() in D:
#
# The super() function in D tries to call the next class in the MRO (Method Resolution Order), which is B.
# Call to super().__init__() in B:
#
# Inside B.__init__(), super() is called, which normally would refer to A because B inherits from A.
# Expected Behavior:
#
# However, in the case of D(B, C), due to multiple inheritance, the next class to be called (after B) should be C, not A—because C is listed in D's inheritance declaration.
# The Problem:
#
# The real issue arises from the fact that both B and C inherit from A in some form, which causes a conflict in the inheritance chain. Python's MRO can't decide how to handle this situation consistently because C should also call B according to your setup, but B already calls A.
# The MRO Error:
#
# Python gets confused in resolving this order, and it throws an MRO inconsistency error. The conflict arises because Python can't decide whether A should be called from B first or from C. So, the MRO is ambiguous, which is why the error occurs.

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(B):
    def __init__(self):
        print("C")
        super().__init__()

class D(C, B):
    def __init__(self):
        print("D")
        super().__init__()

d = D()
print(D.__mro__)

