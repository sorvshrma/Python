class A():
    def __init__(self):
        print("I am class A")
    def age(self):
        print("My age is 8")

class B():
    def __init__(self):
        print("I am class B")
    def age(self):
        print("My age is 10")

class C(A,B):
    def __init__(self):
        print("I am C class")
        super().__init__()

obj = C()
obj.age()