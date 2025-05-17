import re
import pandas as pd
import requests
import bs4

url = "https://www.klook.com/zh-TW/blog/recommended-restaurants-taichung-taiwan/"

web = requests.get(url)
html = bs4.BeautifulSoup(web.text , 'lxml')
text = str(html.text)
# print(text)

blocks = re.split(r"➤", text)

data = []
for block in blocks:
    block = block.strip()

    if not block:
        continue

    name_match = re.match(r"([^\n：\r]{2,50})", block)
    name = name_match.group(1).strip() if name_match else "N/A"

    
    addr_match = re.search(r"地址：?\s*(台中市[^\n，。；]{5,40})", block)
    address = addr_match.group(1).strip() if addr_match else "N/A"

    
    phone_match = re.search(r"(?:電話：)?\s*(\(?04\)?[-\s]?\d{3,4}[-\s]?\d{3,4})", block)
    phone = phone_match.group(1).strip() if phone_match else "N/A"

    data.append([name, address, phone])

df = pd.DataFrame(data, columns=["店家名稱", "地址", "電話"])
df.to_csv("contact_info.csv", index=False)
print('Already convert to csv')
