import requests
import bs4


if __name__ == "__main__":
    url = 'https://post.mmh.org.tw/nursing/?cat=3'

    # headers = {'Headers' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"}
    web = requests.get(url)
    html = bs4.BeautifulSoup(web.text , 'lxml')
    # print(html)

    # url = html.find_all('a' , target = '_blank')
    url = html.select('textwidget')

    for i in url:
        print(i.text)