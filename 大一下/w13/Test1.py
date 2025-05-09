import re 

text = 'My numbers are 123-456-7890 and 987-654-3210'
matches = re.findall(r"\d{3}-\d{3}-\d{4}" , text)
for item in matches:
    print(item)