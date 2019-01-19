import config
from bs4 import BeautifulSoup as bs
from datetime import datetime
import googlemaps
import requests
import json


# gmaps = googlemaps.Client(key=config.maps_key)
# geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
# print(geocode_result)

def check_open(dining_hall_name, menu_time):
	return True


def get_meal_time():
	time = datetime.now()
	time_seconds = (time - time.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	print(time_seconds)


def scrape_dining_hall(dining_hall_name, menu_time = None):
	results = []
	urls = {
		"Cowell/Stevenson": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=",
		"9/10": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=",
		"Rachel Carson/Oakes": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=",
		"Crown/Merrill": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=",
		"Porter/Kresge": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=15&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag="
	}
	if not menu_time:
		menu_time = get_meal_time()
	if not check_open(dining_hall_name, menu_time):
		return ("Sorry,", dining_hall_name, "is closed.")
	else:
		soup = bs(requests.get(urls[dining_hall_name]).content, 'html.parser')
		menu_items = soup.findAll("table", {"border": "0", "width": "100%", "height": "100%"})

		for item in menu_items:
			if item.div.string == menu_time:
				menu_data = item.findAll("span", {"style": "color: #000000"})
				for label in menu_data:
					if len(label.string) != 1:
						results.append(label.string)
	return results

url = "https://sho-prod.ucsc.edu/shs/common/login/stu_login.cfm"
data = {"screenwidth": "0", "screenheight": "0", "LoginAction": "email", "username": config.username, "password": config.password, "login": "Log In"}
r = requests.post(url = url, data = data)
print(r.text) 
print(scrape_dining_hall("9/10", "Dinner"))