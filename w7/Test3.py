txt = ['NTU','NCHU','FCU','CYUT','FCU','FCU']
a = 'FCU'
count = 0 
b = 0
while a in txt[b:]:
    count += 1
    if txt[b: ].index(a) == len(txt) - 1:
        break   
    else:
        b = txt[b:].index(a) + 1 
print(count)
