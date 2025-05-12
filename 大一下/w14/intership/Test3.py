import requests
import bs4

def get_html(url):
    web = requests.get(url)
    print(web)

if __name__ == "__main__":
    url = 'https://eatathome.hoyastore.com'
    web = requests.get(url)
    print(web)