import requests
import bs4
import pandas as pd

if __name__ == "__main__":
    
    target = input("請輸入想查詢的書名關鍵字: ")

    url = 'https://search.books.com.tw/search/query/key/' + target
    headers = {"Headers" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

    html = requests.get(url)
    web = bs4.BeautifulSoup(html.text, 'lxml')
    book_titles = web.select('a[target="_blank"]')
    authors = web.select('.type.clearfix')
    prices = web.select('.price.clearfix')
    
    # print(f'書名數量: {len(book_titles)}')
    # print(f'作者數量: {len(authors)}')
    # print(f'價格數量: {len(prices)}')

    final_data = [] 
        
    for i in range(len(book_titles)):
        title = book_titles[i].get('title', '')
        if i < len(authors):
            author = authors[i].text
        else:
            continue
        if i < len(prices):
            price = prices[i].text
        else:
            continue
        
        data = {'書名' : title , '作者' : author , '價格' : price}
        final_data.append(data)  

    
    df = pd.DataFrame(final_data)
    print(df)
    df.to_csv('Answer.csv')

