dictionaryExample = {
    'name' : 'Sourav',
    'college' : 'Northeastern University',
    'subject' : 'python'
}

print(dictionaryExample)

print (dictionaryExample['name'])
del dictionaryExample['name']
print(dictionaryExample)
dictionaryExample['name'] = 'Kanchan'
print (dictionaryExample.get(1))
print(dictionaryExample)
print(dictionaryExample.keys())
print(dictionaryExample.values())
print(dictionaryExample.__len__())
print(dictionaryExample.get('name'))

ans = (lambda z:z**3)
print(ans(7))