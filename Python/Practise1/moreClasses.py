class myClass():
    age = 90
    def __init__(self):
        self.age = 20;
        self.age = 24;
        self.__myPrivate=("My name is Sourav")
        self._myProtected = ("I am protected")
        self.myPublic = ("I am public")
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

obj1 = myClass()
#obj1.age = 70;
obj2 = myClass()

if obj1.compare(obj2):
    print("Same" + " " + str(obj1.age))
else:
    print("Not Same")



print(obj1._myProtected)
print(obj2._myClass__myPrivate)