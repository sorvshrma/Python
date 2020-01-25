def hello(name, num1):
    print("My name is : " + name + " Age is :" + str(num1))

def student(num):
    return num*num+num

hello("Sourav", 27)
hello("Kanchan", 24)


printResult = student(4)
print(printResult)

is_male = True
is_tall = True
if is_male and is_tall:
    print("Person is male")
elif is_male and not(is_tall):
    print("Male but not tall")
else:
    print("Person is female")

def compare(num1,num2,num3):
    if num1 >= num2 and num2 >= num3:
        return num1,num2
print(compare(4,3,2))

number1 = float(input("Enter First Number = "))
Operator = input("Enter Operator = ")
number2 = float(input("Enter Second Number = "))
if Operator == "+":
    print(number1 + number2)
elif Operator == "-":
    print(number1 - number2)
elif Operator == "/":
    print(number1 / number1)
else :
    print("Invalid Operator")

monthFinderDictionary = {
    "Jan": "January",
    "Feb": "February",
    1: "One"

}
print(monthFinderDictionary.get("Jan"))

i = 0
while(i<=10):
    print(i)
    i+=1
print("Done with while loop")

secret_word = "Sexy"
guess_word = ""
guess_limit = 3
guess_count = 0
out_of_guess = False
while guess_word != secret_word and not(out_of_guess):
    if guess_limit < guess_count :
        guess_word = input("Guess the word : ")
        guess_count += 1
    else:
        out_of_guess = True
if out_of_guess:
    print("You Loose!")
else:
    print("You win!")
