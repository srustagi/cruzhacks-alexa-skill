from bs4 import BeautifulSoup as bs 
import requests

# url = "https://google.com"
# soup = bs(requests.get(url).content, 'html.parser')

menu = ["hell soup", "hasdaaa"]
result = []
for item in menu:
	for bad in non_entrees:
		if (bad in item):
			result.append(item)
print([x for x in menu if x not in result])