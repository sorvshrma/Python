square = lambda z : z**2
print(square(3))

list1 = [1,2,3,4,5]
cube = list(map(lambda z:z**3,list1))
print(cube)

list2 = [-1,-5,-6,-9,0,1,5,3,6,7]
filt = tuple(filter(lambda z: z<0 , list2))
print(filt)

print(id(list2[3]))
print(id(list2[2]))