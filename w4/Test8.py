n = int(input())
count = 0

for i in range(1,n+1):
    if int(i) % 3 == 0:
        count += int(i)
    

print(count)
