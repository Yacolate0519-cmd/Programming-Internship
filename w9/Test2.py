data1 = [1,2,3]
data2 = ['a','b','c']
data3 = ['魯夫','那美','索隆']

newList = []

data = list(zip(data1,data2,data3))

for i in range(len(data)):
    newList.extend(data[i])

print(newList)