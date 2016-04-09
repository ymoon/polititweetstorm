
#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------
import json
import re
import operator
from twitter import *

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
def get_top_politcal_topics():
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
	# query = twitter.search.tweets(q = "from:CNNPolitics", geocode = "37.781157,-122.398720,250mi", result_type = "recent", include_entities = "false", count = 100)

	stop_words = {}
	infile = open("stopwords.txt")
	words = infile.readlines()
	for word in words:
		stop_words[word[:-1]] = True

	query = twitter.search.tweets(q = "from:CNNPolitics", include_entities = "false", count = 100)
	query2 = twitter.search.tweets(q = "from:NBCPolitics", include_entities = "false", count = 100)
	query3 = twitter.search.tweets(q = "from:HuffPostPol", include_entities = "false", count = 100)
	query4 = twitter.search.tweets(q = "from:NPRPolitics", include_entities = "false", count = 100)

	#-----------------------------------------------------------------------
	# How long did this query take?
	#-----------------------------------------------------------------------
	# print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])
	# print json.dumps(query, indent=2)

	#-----------------------------------------------------------------------
	# Loop through each of the results, and print its content.
	#-----------------------------------------------------------------------
	regex = re.compile('[^a-zA-Z]')
	tweets = []
	all_tweets = ""
	stop_words["rt"] = True
	stop_words["https"] = True
	stop_words["http"] = True

	# with open("politicalterms.txt", "a") as myfile:
	# 	for result in query["statuses"]:
	# 		myfile.write(result["text"].encode("utf-8") + "\n")
	frequencies = {}
	count = 0
	for result in query["statuses"]:
		count += 1
		all_tweets += result["text"].encode("utf-8") + " "

	for result in query2["statuses"]:
		count += 1
		all_tweets += result["text"].encode("utf-8") + " "

	for result in query3["statuses"]:
		count += 1
		all_tweets += result["text"].encode("utf-8") + " "

	for result in query4["statuses"]:
		count += 1
		all_tweets += result["text"].encode("utf-8") + " "

	all_tweets = re.sub('https\S+', " ", all_tweets)
	all_tweets = re.sub('\W'," ", all_tweets)
	for word in all_tweets.split():
		if (not stop_words.get(word.lower(), False)):
			frequencies[word.lower()] = frequencies.get(word.lower(), 0) + 1

	sorted_frequencies = sorted(frequencies.items(), key=operator.itemgetter(1), reverse= True)

	# count1 = 0
	# while count1 < 20:
	# 	print sorted_frequencies[count1]
	# 	count1 += 1
	#return list of top tweets - deal with top 20 elsewhere
	return sorted_frequencies

