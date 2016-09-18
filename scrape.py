from bs4 import BeautifulSoup

import sys

from sys import argv
script, place, rent = argv

import requests

url = 'https://washingtondc.craigslist.org/search/apa'

rent = int(rent)

i = 0
numberOfResults = 0

checkForRent = rent > 0

while i < 2500:
    url = 'https://washingtondc.craigslist.org/search/apa?query=' + place
    url = url if (i < 1) else url + '?s=' + str(i)
    page = requests.get(url)
    
    if page.status_code == 200:

        soup = BeautifulSoup(page.content, 'html.parser')

        posts = soup.find(id="sortable-results").div

        for post in posts:
        	link = ""
        	price = ""
        	title = ""
        	location = ""
        	if post.find('span') > 0:
        		link = 'https://washingtondc.craigslist.org' + post.find('span').find('a')['href']

        		price = post.find('span').findAll('span',{'class','price'})

        		if len(price) > 0:
        			price = int(post.find('span').findAll('span',{'class','price'})[0].get_text().strip('$'))
        		title = post.find('span').find(id="titletextonly").get_text().lower()

        		location = post.findAll('span',{'class':'l2'})[0].get_text().lower()

        		if (place in location or place in title):
        			if price <= rent:
        				numberOfResults += 1
        				print title
        				print link
        				print location
        				print '$' + str(price)
        				print "ALERT!! THIS ONE IS IN YOUR BUDGET!"
        				print u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525'
        				print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    	i+=100
    else:
    	print page.status_code
    	i = 10000
print "Complete! Found " + str(numberOfResults) + " new results in " + place + "."
