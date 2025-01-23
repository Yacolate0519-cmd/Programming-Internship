def draw(n,c):
    for i in range(n):
        for j in range(n - i -1):
            print(c,end = '')
        print()  
    
n , c = input("Enter the value: ").split()
draw(int(n),c)