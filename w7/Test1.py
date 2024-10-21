list1 = list(map(int,input().split(',')))

avg = 0
max = list1[0]
min = list1[0]
for i in range(len(list1)):
    avg += list1[i]
avg /= len(list1)

for i in range(len(list1)):
    if list1[i] >= max:
        max = list1[i]

for i in range(len(list1)):
    if list1[i] <= min:
        min = list1[i]

print("平均: ",avg)
print("max: ",max)
print('min: ',min)
'''
23,45,75,100,95,88,55
'''