data1 = [8.0,7.5,3.1,-8,199]
data2 = data1.copy()
data3 = data1.copy()
print(f"Befroe sort data: {data1}")
data1.sort()
print(f"After sort data: {data1}")

print("--"*30)

print(f"Before sort data2: {data2}")
print(f"After sort data: {data2}")

print("--"*30)

print(f"Before sort data3 : {data3}")
data3.sort(reverse=True)
print(f"After sort data3: {data3}")

print("--"*30)