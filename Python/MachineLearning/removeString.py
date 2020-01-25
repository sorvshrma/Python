str1 = 'Sourav'
str2 = 'ou'

# if str1.endswith(str1):
#     s = str1 [:-(len(str2))]

if str2 in str1:
    s = str1.replace(str2, '')
    print(s)
else:
    print('No match')

