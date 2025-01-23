data = ['FCU','NTU','NCKU']
data1 = ["MIT",23]
dict1 = {'name':'Jack','age':25}
print(f"Before extend: {data}")
data.extend(dict1)
print(f"After extend: {data}")
print('--'*30)
data = ['FCU','NTU','NCKU']
print(f"Before append: {data}")
data.append(dict1)
print(f"After append: {data}")
