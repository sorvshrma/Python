import datetime

class Sourav:
    def __init__(self, full_name , birthday):
        self.name = full_name
        self.birthday = birthday

    def age(self):

        today = datetime.date(2019, 5, 10)
        year = int(self.birthday[0:4])
        month = int(self.birthday[4:6])
        day = int(self.birthday[6:8])
        dob = datetime.date(year , month , day)
        print(dob)
        ageInDay = (today - dob).days
       # print(ageInDay)
        ageInYear = ageInDay / 365
        return float(ageInYear)
      #  return age



sourav = Sourav("Sourav Sharma" , "19921012")
print(sourav.name , " " ,  sourav.birthday)
print("age : " , " " , sourav.age())

#help(int)




