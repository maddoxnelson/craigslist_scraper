#imports module info needed
import sys
import json
import requests
#import emoji  #was one idea to impliment the fire.

#takes three command-line args, no seperators
from sys import argv
script, place, rent = argv #fill variables with values from command prompt.

#sets up variables used in script.
url = 'https://washingtondc.craigslist.org/jsonsearch/apa/?query=' + place
rent = int(rent)

numberOfResults = 0

#fetch json stuff
page = requests.get(url) #fetches a "response" object called 'page'.
page = page.json() #makes the page response become json.
contents = page #simpler than python 2...because contents are already json...or something.

#script
for item in contents:
	for thing in item:
		post = json.dumps(thing, sort_keys=True, indent=4, separators=(',', ': '))
		if "PostingTitle" in json.loads(post):
			numberOfResults += 1 #increments numberOfResults to print total, below.
			print(json.loads(post)["PostingTitle"])
			if "PostingURL" in json.loads(post):
				print(json.loads(post)["PostingURL"])
			if "Ask" in json.loads(post):
				print('$' + str(json.loads(post)["Ask"]))
				if (int(json.loads(post)["Ask"]) <= rent):
					print("ALERT!! THIS IS IN YOUR BUDGET!")
				#	print(u'\U0001f525')  #temporarily disabling
			print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print("Complete! Found " + str(numberOfResults) + " new results in " + place + ".")
