data = list(range(10,0,-1))
print(data)
data2 = list(range(1,11))
print(data2[::-1])

data = [1,2,3,2,1]

for i in range(len(data)):
    if data[i] == data[:-i+1]:
        print("true")
    else:
        print('false')