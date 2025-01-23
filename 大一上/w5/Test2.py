# n = int(input())
total = 0
count = 0 
    
while True:
    n = int(input())
    if n == -999:
        break
    total += n
    count += 1    
    
    
print("多少數字: ",count)
print('組合: ',total)
print("平均: ", (total / count))

'''
#第二種程式碼
n = 0
total = 0
val = 0
while n != -999:
    n += 1
    total += n
    n = int(input())
print(n)
print(total)
print((total / n))
'''

