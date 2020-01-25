def sumOfSqare(n):
    x = 0
    for i in range (1 , n+1):
        x = x + i**2
    return x

print(sumOfSqare(5))