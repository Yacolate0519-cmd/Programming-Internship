n = 0 
for i in range(3):
    for j in range(4):
        n += 1
        if n == 7:
            continue
        print(f'{n:3d}',end = '\t')
    print('\n')
    if n >= 8:
        break #此break會讓done印不出來
else:
    print("done")  
    