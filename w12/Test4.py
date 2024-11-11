import sys

if __name__  == '__main__':
    print(f'content in argv list = {sys.argv}')
    if len(sys.argv) != 4:
        print('Error')
    elif sys.argv[1] == 'Enc':
        data = []
        code = ''
        temp = list(sys.argv[3])
        for i in temp:
            a = ord(i) + 3
            data.append(chr(a))
        code = ''.join(data)
        print(f'Encrypted text = {code}')
    elif sys.argv[1] == 'Dec':
        temp = list(sys.argv[3])
        code = ''
        data = []
        for i in temp:
            a = ord(i) - 3
            data.append(chr(a))
        code = ''.join(data)
        print(f'Encrypted text = {code}')