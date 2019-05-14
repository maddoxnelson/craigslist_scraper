import requests
from sys import argv # takes three command-line args, no seperators
# import emoji  # was one idea to impliment the fire.


# fill variables with values from command prompt.
rent = argv[-1]
loc = argv[1:-1]
place = ' '.join(loc)

# sets up variables used in script.
url = "https://washingtondc.craigslist.org/jsonsearch/apa/?query=" + place
rent = int(rent)

numberOfResults = 0

# fetch json stuff
page = requests.get(url)  # fetches a "response" object called 'page'.
contents = page.json()  # makes the page response become json.

# script
listings = contents[0]
for thing in listings:
    posting = thing.get("PostingTitle")
    if posting:
        numberOfResults += 1  # increments numberOfResults to print total, below.
        print(posting)
        PostingURL = thing.get("PostingURL")
        Ask = thing.get("Ask")
        if PostingURL:
            print(PostingURL)
            if Ask:
                print("$" + str(Ask))
                print("ALERT!! THIS IS IN YOUR BUDGET!")
            else:
                print("Look at posting for price")
            # 	print(u'\U0001f525')  #temporarily disabling
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Complete! Found " + str(numberOfResults) + " new results in " + place + ".")
