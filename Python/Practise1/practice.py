list = [11,45,76,6,7,8,9]
list2 = list + [12,23,34,45]

print(list2[0:2])
list3 = [x**2 for x in [1,2,3,4]]
print(list2)
list4 = []
for i in [2,3,4,5,6]:
    list4.append(i**2)
list2.sort()
print(list2)
print(list4)

tup = ([1,2,3,4,5], [56,56,34,23])

print(tup[1][0:3])

string = "My name is Sourav"

print('R' in string)

