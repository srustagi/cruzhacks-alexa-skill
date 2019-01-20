from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests

def get_meal_time(dining_hall_name):
	time = datetime.now()
	time_seconds = (time - time.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
	if time.weekday() == 5 or time.weekday() == 6:
		if time_seconds > 25200 and time_seconds < 36000:
			return "Breakfast"
		elif time_seconds > 36000 and time_seconds < 61200:
			return "Lunch"
		elif time_seconds > 61200 and time_seconds < 82800:
			return "Dinner"
	else:
		if time_seconds > 23400 and time_seconds < 41400:
			return "Breakfast"
		elif time_seconds > 41400 and time_seconds < 61200:
			return "Lunch"
		elif time_seconds > 61200 and time_seconds < 82800:
			return "Dinner"


def scrape_dining_hall(dining_hall_name, menu_time = None):
	results = []
	urls = {
		"Cowell/Stevenson": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell+Stevenson+Dining+Hall&sName=&naFlag=",
		"9/10": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&sName=&naFlag=",
		"Rachel Carson/Oakes": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=",
		"Crown/Merrill": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill+Dining+Hall&sName=&naFlag=",
		"Porter/Kresge": "https://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=15&locationName=Porter+Kresge+Dining+Hall&sName=&naFlag="
	}
	non_entrees = ["Natural Bridges", "Hash Brown", "Eggs", "Bisque", "Cheese Pizza", "Pepperoni Pizza", "Oven Roasted", "Muffin", "Donut", "Croissaint", "Condiments", "Okra", "Squash", "Plantains", "Carnitas", "Beans", "Rice", "Cappuccino", "Soup", "Onion Rings", "Fries", "Seasonal Vegetable", "UCSC Bakery French Rolls", "Mousse", "Samosa", "Naan", "Cookie", "Sauce", "Relish"]
	if not menu_time:
		menu_time = get_meal_time(dining_hall_name)
	else:
		soup = bs(requests.get(urls[dining_hall_name]).content, 'html.parser')
		menu_items = soup.findAll("table", {"border": "0", "width": "100%", "height": "100%"})

		for item in menu_items:
			if item.div.string == menu_time:
				menu_data = item.findAll("span", {"style": "color: #000000"})
				for label in menu_data:
					if len(label.string) != 1:
						results.append(label.string)
	clean_menu = []
	for item in results:
		for bad in non_entrees:
			if (bad in item):
				clean_menu.append(item)
	return [food for food in results if food not in clean_menu]
