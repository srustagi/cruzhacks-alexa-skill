# Forest Alexa CruzHacks Submission
Shivansh Rustagi, Kamil Kisielewicz, Ming Jeng

## Inspiration
* As busy students with a lot of goals and aspirations, we felt like this would be an application critical to our own success. Time is the only thing that's limited, and having tools to make our lives more efficient opens a pathway to our dream life.

## What it does
* Forest is an Amazon Alexa skill with a serverless Python backend integrated with AWS Lambda intended to give UCSC students immediate access to information regarding the dining hall system and their personal accounts. We scraped information from dining hall websites and the UCSC housing portal to implement our application.

## How we built it
* Our application is separated into two components: the Amazon Alexa service which takes user voice as input and the AWS Lambda backend which processes the natural language input to provide a response. 
* We made sure to include a variety of "synonyms" for our intents, allowing our users to refer to locations by their common names
	* For example, Alexa would process "What's for dinner at College 8" and "What does Rachel Carson have for 
dinner" in the same way.

## Challenges we ran into
* The latest Python version that runs with BeautifulSoup is Python 3.2. Since AWS Lambda only allowed 2.7, 3.6, and 3.7, we were forced to downgrade our code to Python 2.7. Upon realizing this, we were able to fix all the lambda integration bugs and flesh out the remaining syntax errors with ease
* Scraping the data from antiquated websites was difficult, as we had to deal with poorly structured DOM elements and depreciated technology such as iframes. 
	* Furthermore, with no access to APIs, we accessed all of the encrypted data behind the UCSC secure system by piggybacking HTTP requests.
* We didn't want to include repetitive items such as desserts and pizza into our menu, and instead wanted to focus on the entrees which are cycled out every day. We ended up using Python list comprehensions to achieve this feature

## Accomplishments we're proud of
* Solving all the scraping problems 
* Solving AWS Lambda and Alexa integration problem with python version mismatch

## What we learned
* Regex
* How to build an Alexa skill
* Serverless computing!

## What's next for Forest
* After Cruzhacks, we will publish the skill on the Amazon Alexa Skills Marketplace, allowing students to use the app
* We plan to create iPhone and Android mobile apps with extended feature sets such as adding location and purchase functionality
