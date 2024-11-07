# def gcd(a , b):
#     for i in range(1 , a ):  
#         if a % i == 0 and b % i == 0:
#             return gcd(int(a/i),int(b/i))
        
    
# print(gcd(48,18))

def cd(n):
    data = []
    for i in range(n,0,-1):
        if n % i == 0:
            data.append(i)
    print(data) 
    return data
n = 48
m = 18
# print(cd(n),cd(m))

cd(n)
cd(m)


all = []

for i in cd(m):
    
print(cd(n) and cd(m))