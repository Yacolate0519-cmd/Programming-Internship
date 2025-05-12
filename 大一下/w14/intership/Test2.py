import requests
import bs4
import re

url = "https://www.104.com.tw/company/10qbb4w0?jobsource=google"

web = requests.get(url)
html = bs4.BeautifulSoup(web.text , 'lxml')

links = html.find_all('p' , 'r3 mb-0 text-break')
links = str(links)

# urls = re.findall(r'http(\S)+' , links)
urls = re.findall(r'https?://[^\s\'">]+', links)
for i in urls:
    print(i)

