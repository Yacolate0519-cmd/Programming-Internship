# list1 = list(map(int,input().split(',')))

# avg = 0
# max = list1[0]
# min = list1[0]
# for i in range(len(list1)):
#     avg += list1[i]
# avg /= len(list1)

# for i in range(len(list1)):
#     if list1[i] >= max:
#         max = list1[i]

# for i in range(len(list1)):
#     if list1[i] <= min:
#         min = list1[i]

# print("平均: ",avg)
# print("max: ",max)
# print('min: ',min)
'''
23,45,75,100,95,88,55
'''

data = list(map(int,input().split(',')))
avg = 0
max = data[0]
min = data[0]

for i in range(len(data)):
    avg += data[i]
avg = round(avg / len(data),2)

for i in range(len(data)):
    if data[i] >= max:
        max = data[i]
for i in range(len(data)):
    if data[i] <= min:
        min = data[i]
print(f"平均{avg}\nmax = {max}\nmin = {min}")