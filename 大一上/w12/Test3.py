import sys

def check(x):
    if x <= 0:
        return 1
    else:
        return x * check(x - 1)

if __name__ == '__main__':
    print(f'content in argv list : {sys.argv}')
    if len(sys.argv) != 2:
        print('Error')
    else:
        print(f'{sys.argv[1]}! = ',check(int(sys.argv[1])))