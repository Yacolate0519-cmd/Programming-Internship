def fabonaic(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fabonaic(n-1) + fabonaic(n-2)
    
n = int(input("Enter the number: "))
print(fabonaic(n))