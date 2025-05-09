import re

txt = 'The price is $123'

match = re.search(r"\$(\d+)" , txt)
match1 = re.search(r"(\$\d+)" , txt)

if match:
    price = match.group(1)
    price1 = match1.group(1)
    print(f"The price is: {price}")
    print(f"The price is: {price1}")
