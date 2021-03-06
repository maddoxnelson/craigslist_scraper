import sys
import json
import requests

from sys import argv
script, place, rent = argv

url = 'https://washingtondc.craigslist.org/jsonsearch/apa/?query=' + place
rent = int(rent)

numberOfResults = 0
page = requests.get(url)
contents = json.loads(str(page.content))

for item in contents:
	for thing in item:
		post = json.dumps(thing, sort_keys=True, indent=4, separators=(',', ': '))
		if "PostingTitle" in json.loads(post):
			numberOfResults += 1
			print json.loads(post)["PostingTitle"]
			if "PostingURL" in json.loads(post):
				print json.loads(post)["PostingURL"]
			if "Ask" in json.loads(post):
				print '$' + str(json.loads(post)["Ask"])
				if int(json.loads(post)["Ask"]) <= rent:
					print "ALERT!! THIS IS IN YOUR BUDGET!"
					print u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525',u'\U0001f525'
			print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

print "Complete! Found " + str(numberOfResults) + " new results in " + place + "."
