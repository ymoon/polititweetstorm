import json
import re
import operator
from twitter import *

def grab_tweets(topic, location):
	
	#Load the twitter api information
	config = {}
	execfile("config.py", config)

	lat = str(location[0])
	lng = str(location[1])
	radius = "20mi" #subject to change, just for testing
	location = lat + ',' + lng + ',' + radius

	#configure
	twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

	#Search for tweets in a specific location that contain a certain topic (passed as paramaters)
	#keyword, coordinates, english, return 100 (this is the max), no need to inlcude entities because hashtag aleady included in text
	return twitter.search.tweets(q = topic, geocode = location, lang = "en", count = 100, include_entities = "false")





