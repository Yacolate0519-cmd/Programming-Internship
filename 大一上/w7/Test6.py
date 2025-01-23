#append()
data = ['FCU','NTU','NCKU']
data1 = [45,67]
data.append(data1)
print(f'data: \n{data}')

print(data[3][0])

#extend()
data3 = ['FCU','NTU','NCKU']
data4 = [45,67]
data3.extend(data4)
print(data3[3])