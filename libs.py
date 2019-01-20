from bs4 import BeautifulSoup as bs 

url = "https://google.com"
soup = bs(requests.get(url).content, 'html.parser')
print(soup)