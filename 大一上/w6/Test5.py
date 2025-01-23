n = int(input("請輸入一個正整數: "))

total = 1

if n < 0:
    print("請輸入一個有效的正整數")
else:
    for i in range(n,1,-1):
        total *= i
    print(f'{n}! = ',total)

