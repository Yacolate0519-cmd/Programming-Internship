n = int(input())
for i in range(n):
    for j in range(n):
        if 1 <= i <= n-2 and 1 <= j <= n-2:
            print(' ',end = '')
        else:
            print('#',end = '')
    print()