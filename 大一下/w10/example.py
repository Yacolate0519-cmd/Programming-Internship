import requests 
import bs4

if __name__ == "__main__":
    
	url = 'https://udn.com/news/story/6811/8725074'

	request = requests.get(url)
	
	html = bs4.BeautifulSoup(request.text , 'html.parser')

	# print(html)

	# content = html.find_all('section' ,  'article-content__editor')
	content = html.find_all('h3' , 'rounded-thumb__title')

	for i in content:
		print(i.get_text(strip=True))
		# print(i.text)