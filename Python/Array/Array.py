friends = ["a","v","r"]

for a in range(len(friends)):
    if a ==1:
        print("secound value")
    else:
        print("other values")

def multiply(number , times):
    r = 1
    for value in range(times):
        r = r * number
    return r

print(multiply(3,3))

list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for a in list:
    for b in a:
        print(b)

# If function and for loop

try:
    i = 10/0;
    number = int(input("Enter the number"))
    print(number)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError as err:
    print(err)


def func(line):
    vowel = ["a","e","i","o","u"]
    translate = ""
    for a in line:
        if a.lower() in vowel:
            if a.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:
            translate = translate + a
    return translate
print(func(input("Enter the string")))



readtext = open("hello.txt","r")
#readtext.write("\nAdding another line for testingg  ")
#print(readtext.readlines())

import Array1

Array1.function1()

writeToNewFile = open("newFile.html", "w")
writeToNewFile.write("This is new File")
writeToNewFile.close()
