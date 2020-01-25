def prime(n):
    if n <= 1:
        return 'Not prime number'
    else:
        for i in range (2 , n//2):
            if (n % i ) == 0:
                return 'not prime number'
                break
        else:
            return 'prime'

print(prime(9))
