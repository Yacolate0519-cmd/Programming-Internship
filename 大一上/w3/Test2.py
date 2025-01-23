a , b , c = map(int,input().split())

if(a <= b <= c):
    if(a+b)>c:
        print("True")
    else:
        print("NO")
else:
    print("False")