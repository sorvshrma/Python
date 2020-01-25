class getset():
    def __init__(self,coursename):
        self.coursename = coursename

    def setCourse_Name(self,coursename):
        self.coursename = coursename

    def getCourse_Name(self):
        return(self.coursename)

obj = getset("mASTER")

print(obj.getCourse_Name())

obj.setCourse_Name("sourav")

print(obj.getCourse_Name())