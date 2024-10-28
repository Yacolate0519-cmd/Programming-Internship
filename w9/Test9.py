dict1 = {'name':'Jack','dept':'AITA'}

dict2 = dict1.copy()

dict1['dept'] = 'CSIE'
print(dict2['dept'])

print('--'*30)

dict2 = dict1
dict1['dept'] = 'CSIE'
print(dict2['dept'])
