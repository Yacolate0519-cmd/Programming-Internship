import sys

if __name__ == "__main__":
    print(f'content in argc list : {sys.argv}')
    if len(sys.argv) <= 4:
        if sys.argv[2] == '+':
            print(f'{sys.argv[1]} + {sys.argv[3]} = {int(sys.argv[1]) + int(sys.argv[3])}')
        elif sys.argv[2] == '-':
            print(f'{sys.argv[1]} - {sys.argv[3]} = {int(sys.argv[1]) - int(sys.argv[3])}')
        elif sys.argv[2] == 'x': #因為*在軟體中是萬用字元，所以使用*無法執行
            print(f'{sys.argv[1]} x {sys.argv[3]} = {int(sys.argv[1]) * int(sys.argv[3])}')
        elif sys.argv[2] == '/':
            print(f'{sys.argv[1]} / {sys.argv[3]} = {int(sys.argv[1]) / int(sys.argv[3])}')
        elif sys.argv[2] == '%':
            print(f'{sys.argv[1]} % {sys.argv[3]} = {int(sys.argv[1]) % int(sys.argv[3])}')
        elif sys.argv[2] == '^':
            print(f'{sys.argv[1]}^{sys.argv[3]} = {int(sys.argv[1]) ** int(sys.argv[3])}')
    else:
        print('Wrong input')