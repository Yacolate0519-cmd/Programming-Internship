height , sex = map(int,input().split())

if sex == 1:
    res = (height-80) * 0.7 
elif sex == 2:
    res = (height - 70) * 0.6
else:
    print("Input Error")
print(f'{res:.02f}')
    