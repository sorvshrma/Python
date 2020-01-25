class call():
    a = 5
    b = "Sourav"
    def __priFunc(self):
        print("i am private")
    def _proFunc(self):
        print("I am protected")
    def pubFunc(self):
        print("I am public")
ob = call()
ob1 = call()
ob._call__priFunc()
ob._proFunc()
ob.pubFunc()
print(str(ob.a) + " " + ob.b)

ob.a=6
print(str(ob.a) + " " + str(ob1.a))

