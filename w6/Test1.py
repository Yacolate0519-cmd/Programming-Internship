total = 0
count = 0
while True:  
    n = input("請輸入成績: ")
    
    if n.isdigit():
        n = int(n)
        if 100 >= n >= 0:
            total += n
            count += 1
    elif n == '-1':
        break
    else:
        print("請輸入有效的數字")
             
    
    
if total == 0:
    print("沒有輸入任何成績")
else:
    print("平均成績為:",total / count)
