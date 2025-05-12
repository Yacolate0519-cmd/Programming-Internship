import re
import requests

url = 'https://post.mmh.org.tw/nursing/?cat=3'
res = requests.get(url)
html = res.text

# links = re.findall(r'<a\s+(?:[^>]*?\s+)?href=["\'](.*?)["\']', html)
links = re.findall(r'href=["\'](.*?)["\']', html)

for link in links:
    print(f'Link = {link}')

mobile = re.findall(r"\(\d{2,4}\)\d{6,8}|\d{6,8}", html)

print('--'*30)

for phone in mobile:
    print(f'Phone = {phone}')