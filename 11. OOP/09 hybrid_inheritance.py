# Combination of hierarchial and multiple inheritance
class A:
    def method1(self):
        print("this is method 1")


class B(A):
    def method2(self):
        print("this is method 2")


class C(A):
    def method3(self):
        print("this is method 3")


class D(B, C):
    def method4(self):
        print("this is method 4")


obj1 = D()
obj1.method1()
obj1.method2()
obj1.method3()
obj1.method4()

