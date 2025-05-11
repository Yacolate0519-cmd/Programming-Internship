import requests
import bs4
from itertools import zip_longest
import pandas as pd

if __name__ == "__main__":
    url = 'https://search.books.com.tw/search/query/key/python/cat/all'
    headers = {'Headers' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36' }
    web = requests.get(url , headers = headers)
    html = bs4.BeautifulSoup(web.text , 'lxml')
    
    Title = []
    Author = []
    Price = []

    #Title
    title = html.find_all('a' , target = '_blank')
    for i in title:
        i = i.text.strip()
        if i:
            Title.append(i)
            
    #Author
    author = html.find_all('p' , 'author')
    for i in author:
        i = i.text.strip()
        if i:
            Author.append(i)

    price = html.find_all('ul' , 'price')
    for i in price:
        i = i.text.strip()
        if i:
            Price.append(i)
        
    books = []

    for title , author , price in zip_longest(Title , Author , Price):
        book = {
            'Title' : title if title else 'N/A',
            'Author' : author if author else 'N/A',
            'Price' : price if price else 'N/A'
        }
        books.append(book)

    pd = pd.DataFrame(books)
    
    pd.to_csv('result.csv')
    
    print('Done')
    