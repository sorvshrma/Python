list = [{1:2},{3:4},{1:2},{8:9},{1:2}]

print('original list : ' , list)

newList = []
for i in range(len(list)):
    if (
            list[i] not in list[i + 1:]
    ) :
        newList.append(list[i])

print(newList)

list = [
    1,2,3,4,5
]

print(list)



