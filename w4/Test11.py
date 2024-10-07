n = int(input("Input: "))
for i in range(5):
    for j in range(5):
        if 1<=i<=3 and 1<=j<=3 :
            print(' ',end=' ')
        else:
            print("#",end = ' ')
    print()