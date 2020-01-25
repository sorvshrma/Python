import sys

class sum():
    def mul(self,a,b):
        try:
            c = a/b
            print(c)
        except:
            print("Exception is : ", sys.exc_info() )

obj1 = sum()
obj1.mul(2,0)
