def Collatz(n):
    count = 0
    while 1:
        print(int(n),end = '')
        if n == 1:
            break
        elif n % 2 == 0:
            n /= 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
        print(' -> ',end = '')
    return count


n = int(input("請輸入一個正整數: "))


print("\n總步數:",Collatz(n))
