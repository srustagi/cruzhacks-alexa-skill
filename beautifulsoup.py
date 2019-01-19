from bs4 import BeautifulSoup
import requests
# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://guides.library.ucsc.edu/libraryhours'
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)

# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.
#textContent = []
#for i in range(0, 20):
	#paragraphs = page_content.find_all("p")[i].text
paragraphs = page_content.find(id="s-lg-content-38442577")
#prettify()
	# textContent.append(paragraphs)
paragraphs.find("p").getText()
print(paragraphs)
# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, 
# and push them into an array so that I can manipulate and do fun stuff with the data.
