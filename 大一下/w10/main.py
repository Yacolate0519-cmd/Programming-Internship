import requests
import bs4
import csv
import pandas as pd

if __name__ == "__main__":
    
    target = input("請輸入想查詢的書名關鍵字: ")

    url = 'https://search.books.com.tw/search/query/key/' + target
    
    # url = 'https://search.books.com.tw/search/query/key/python/cat/all'

    headers = {"Headers" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

    html = requests.get(url)
    web = bs4.BeautifulSoup(html.text ,'lxml')
    result = web.select('.table-td')

    book_titles = web.select('a[target="_blank"]')
    author = web.select('.type.clearfix')
    price = web.select('.price.clearfix')

    print(len(book_titles))
    print(len(author))
    print(len(price))

    # for i in range(len(price)):
    #     data = {'書名': book_titles[i] , "作者" : author[i] , '價格' : price[i]}

    # pd = pd.DataFrame(data)
    
    # print(pd)

    
    for i in book_titles:       
        if i == ' ' or i == '\n':
            continue
        else:
            print(f'書名: {i.text}')
        
    titles = []

    
    for book in book_titles:
        title = book.get('title', '').strip()
        if title:  
            titles.append(title)

    
    for title in titles:
        print(title)



    # for i in book_titles:
    #     print(f'書名: {i.text}')
    # for i in author:
    #     print(f'作者: {i.text}')

    # final_data = []

    # for i in result:
    #     result = i.text.replace('\n' , '')
    #     if result == '試閱' or result == '':
    #         continue
    #     else:
    #         parts = result.split('優惠價')
    #         author_and_price = parts[0].split('中文書')
    #         # print(f'書名: {author_and_price[0]}')
    #         # print(f'作者: {author_and_price[1]}')
    #         # print(f'價格: {parts[1]}')
            
    #         data = {'書名': author_and_price[0], '作者': author_and_price[1], '價格': parts[1]}
    #         final_data.append(data)
            
    # pd = pd.DataFrame(final_data)
    
    # print(pd)

    # pd.to_csv('Answer')
    
        
    