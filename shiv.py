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


def get_nearest_hall():
	print()


def get_meal_time():
	time = datetime.now()
	time_seconds = (time - time.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	print(time_seconds)


def scrape_dining_hall(dining_hall_name = None, menu_time = None):
	weekend = False
	if not dining_hall_name:
		dining_hall_name = get_nearest_hall()
	if not menu_time:
		menu_time = get_meal_time()
	if not check_open(dining_hall_name, menu_time):
		print("Sorry,", dining_hall_name, "is closed.")
		return
	else:
		soup = bs(requests.get("https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=").content, 'html.parser')
		menu_items = soup.findAll("span", {"style": "color: #000000"})
		for i, item in enumerate(menu_items):
			if item is not ' ':
				menu_items[i] = item.string
		print(menu_items)



scrape_dining_hall("eh, hhe", "heh")