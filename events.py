import feedparser
from datetime import datetime as dt
import dateutil.parser

months = {"":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":}
days = {"":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, "":, }


def scrape_events(date):
	results = []
	feed = feedparser.parse("http://rssmix.com/u/8308287/rss.xml")
	for item in feed["items"]:
		if dateutil.parser.parse(item["date"]).date() == date.date():
			results.append(item["title"])
	return results

print(scrape_events(dt(2019, 2, 15)))
