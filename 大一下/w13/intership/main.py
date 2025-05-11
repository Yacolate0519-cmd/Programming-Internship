import requests
import bs4

if __name__ == '__main__':
    url = 'https://search.books.com.tw/search/query/key/python/cat/all'
    headers = {'Headers' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' }
    web = requests.get(url)
    html = bs4.BeautifulSoup(web.text , 'lxml')

    title = html.select('a[target="_blank"]')
    # title = html.select('h4[title]')

    #Title
    # for i in title:
    #     i = i.text.strip()
    #     if title:
    #         print(f'Title = {title}')
    
    for i in title:
        title = i.get('title' , '').strip()
        if title:
            print(f'Title = {title}')

    #Author is Done
    # author = html.select('.author')
    # #Author
    # for i in author:
    #     author = i.text.strip()
    #     if author:
    #         print(f'Author = {author}')
    




