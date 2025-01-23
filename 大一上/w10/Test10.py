#十進位轉二進位

data = []

def circle(x):
    while x  > 0:
        if x % 2 >= 0:
            data.insert(0,x % 2)
            x = x // 2
    return data
 
x = int(input("Enter the number: "))

print(circle(x))

total = 0
for i in data:
    total += int(data[::-1]) * 2 ** (len(data)-i-1)
print(total)
    
    