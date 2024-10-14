n , m = map(int,input().split())
total = 0 
while n <= m:
    if n % 2 != 0:
        total += n
    n+=1
print(total)
