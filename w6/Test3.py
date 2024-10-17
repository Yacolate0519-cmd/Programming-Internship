n = input("輸入: x = ")

list = [0,1,6,8,9]


for i in range(len(n)):
    for j in range(len(list)):
        if int(n) in list:
            print('true')
        else:
            break
print("fault")



# a = (''.join(reversed(n)))

# if a == n:
#     print("true")
# else:
#     print("false")

