while True:
    print("1 = Print name")
    print("2 = caculator")
    print("3 = draw triangle")
    print("q = quit")
    print('--'*30)
    n = input()
    if n == 1:
        print("人工智慧技術與應用學士學位學程")
        print('--'*30)
    elif n == 2:
        i,k = map(int,input().split())
        print(i,'+',k,'=',(i+k))
        print(i,'-',k,'=',(i-k))
        print(i,'*',k,'=',(i*k))
        print(i,'/',k,'=',(i/k))
        print('--'*30)
    elif n == 3:
        m = int(input())
        for i in range(n):
            for k in range(n-i-1):
                print(' ',end = '')
            for j in range(2*i+1):
                print('*',end = '')
            print()
        print('--'*30)
    elif n == 'q':
        break
