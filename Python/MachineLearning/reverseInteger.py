def reverse(x):
    a = 0;
    b = 0;
    while(x>0):
        a = x%10
        x = int(x/10)
        b  =  b*10 + a
    return b

n = int (input('Enter the number : '))
print(reverse(n))

