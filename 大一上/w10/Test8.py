def check(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * check(n-1)
    
    
n = int(input("Enter the number: "))
print(f'{n}! = ',check(n))