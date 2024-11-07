def factorial(n):
    if n == 0:
        return 1
    else:
        val = 1
        for i in range(n,1,-1):
            val *= i
        return val
    
n,m = map(int , input("Enter n and m: ").split())
print(f'{n}!= {factorial(n) / factorial(m) * factorial(n-m)}')        