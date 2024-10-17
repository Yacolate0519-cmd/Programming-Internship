while True:
    print('選擇運算符號(+,-,*,/) : ')
    n = input()

    a = int(input("請輸入第一個數字: "))
    if a == -999:
        print("程式結束")
        break

    b = int(input("請輸入第二個數字: "))

    if n == '+':
        print("結果: " , a, " + " , b , " = ",a+b)
    elif n == '-':
        print("結果: " , a, " - " , b , " = ",a-b)
    elif n == '*':
        print("結果: " , a, " * " , b , " = ",a*b)
    else :
        if b == 0:
            print("不能除以0,請重新輸入")
        else:
            print("結果: " , a, " / " , b , " = ",a/b)
        