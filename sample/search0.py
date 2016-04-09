
#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------
import json
from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------

config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/docs/api/1/get/search
#-----------------------------------------------------------------------
query = twitter.search.tweets(q = "from:CNNPolitics", geocode = "37.781157,-122.398720,250mi", result_type = "recent", include_entities = "false", count = 100)

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])
print json.dumps(query, indent=2)
