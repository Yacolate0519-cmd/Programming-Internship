num = [10,20,30,40,50,60,70,80]
range1 = [(1,4),(3,6),(5,8)]
data = []

for i in range(len(range1)):
    m , n = map(int,range1[i].split(','))
    print(m,',',n)
    # data.extend(num[m:n])

print(data)


# # a,b = map(int,input())
# a,b = map(int,input().split())
# print(a,',',b)

# # extend