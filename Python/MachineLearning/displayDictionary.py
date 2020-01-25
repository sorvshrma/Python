dic = {}

dic[6] = 'Kanchan'
dic[3] = 5
dic[1] = 2
dic[2] = 'Sourav'

print(sorted(dic))

for i in sorted(dic):
    print(i , ':' , dic[i])

dic1 = {2:'Praful',
        7:'Upasana'}

dic.update(dic1)

print(set(dic))


