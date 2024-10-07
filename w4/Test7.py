list = [1,4,9,16,25,36,49]

list1 = [x**2 for x in list]

for i in list1:
    print(int(i) , end = '\t')
    
print('\n','--'*30)

list2 = [i for i in range(1,11) if i % 2 ==1]

for i in list2:
    print(int(i) , end = '\t')