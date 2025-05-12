import requests
import bs4

url = 'https://post.mmh.org.tw/nursing/?cat=3'

headers = {"Headers" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}

web = requests.get(url , headers = headers)
html = bs4.BeautifulSoup(web.text , 'lxml')
# print(html)

# url = html.select('a[target="_blank"]')
url = html.find_all('a','entry-content')

for i in url:
    print(i.text)