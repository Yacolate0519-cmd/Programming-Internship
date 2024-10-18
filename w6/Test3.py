n = input("input: ")
n_str = list(n)

n_str = list(''.join(reversed(n)))


x_str = []

for i in n_str:
    if i == '0':
        x_str.append('0')
    elif i == '1':
        x_str.append('1')
    elif i == '6':
        x_str.append('9')
    elif i == '8':
        x_str.append('8')
    elif i == '9':
        x_str.append('6')
    else:
        print('false')

x_str = (''.join(x_str))

print(f'x = {n}')

if str(x_str) == str(n):
    print('true')
else:
    print("false")
    