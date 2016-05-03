from nltk.tokenize import word_tokenize
from alchemyapi_python.alchemyapi import AlchemyAPI
import nltk
import json
import math

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

# search_results: set of tweets that were returned from the relevant query
# text_to_info: maps the tweet to a tuple of information regarding that tweet (tweet, created, user)
# topic: the topic selected by the user for the query

# Function to calculate and return the overall sentiment of the parsed tweets for the relevant query
def alc_sent_system(search_results, text_to_info, topic):

	# # Lists of example texts
	# pos_examples = []
	# neg_examples = []


	alc = AlchemyAPI()
	alc_neg_count = 0
	alc_pos_count = 0
	alc_sent_score = 0.0

	# Grab the entity of the topic 
	# There should only be one with the unigram/bigram provided
	try:
		ent_topic = alc.entities("text", topic, {'sentiment': 0})["entities"][0]["text"].lower()
		print "valid topic entity", ent_topic
	except:
		# topic has no entity so just grab basic doc text sentiment
		ent_topic = None

	# Loop through search_results to classify each tweet in results
	for tweet in search_results:
		#Look into entity recognition and actually extracting sentiment towards the entity searched for and not just the overall tweet

		if ent_topic:
			# Entity recognition based sentiment analysis
			ent_response = alc.entities("text", tweet, {'sentiment': 1})
			for ent in ent_response["entities"]:
				print ent["text"].lower()
				#check if the entity in the tweet is the same/is within the topic entity or vice versa
				if ((ent["text"].lower() in ent_topic) or (ent_topic in ent["text"].lower())):
					print "entity in tweet was part of topic entity", ent_topic
					# Get Sentiment
					if ent["sentiment"]["type"] == "negative":
						alc_neg_count += 1
					elif ent["sentiment"]["type"] == "positive":
						alc_pos_count += 1
					# Get Sentiment score
        			if  "score" in ent["sentiment"]:
						alc_sent_score += float(ent["sentiment"]["score"])
		else:
			#use alchemyAPI to determine if positive or negative
			sent_response = alc.sentiment("text", tweet)
			#calculate if there are more positive or more negative examples
			if sent_response["docSentiment"]["type"] == "negative":
				alc_neg_count += 1
			elif sent_response["docSentiment"]["type"] == "positive":
				alc_pos_count += 1

			#add sent score value to system to determine overall score
				#when neutral no score is present 
			if  "score" in sent_response["docSentiment"]:
				alc_sent_score += float(sent_response["docSentiment"]["score"])



	# # Creates a list for of json objects of tweets of negative and positive examples
	# for i in range(len(pos_examples)):
	# 	pos_examples[i] = text_to_info[pos_examples[i]]
	# for i in range(len(neg_examples)):
	# 	neg_examples[i] = text_to_info[neg_examples[i]]
	# print pos
	# print pos_examples
	# print neg
	# print neg_examples
	if (alc_pos_count + alc_neg_count > 0):
		pos_percent = (alc_pos_count/float(alc_pos_count+alc_neg_count)) * 100
		neg_percent = (alc_neg_count/float(alc_pos_count+alc_neg_count)) * 100
	else:
		print "Something went wrong/no tweets were found"
		pos_percent = 0
		neg_percent = 0
	print pos_percent
	print neg_percent

	if alc_neg_count > alc_pos_count:
		alc_sent_from_examples = "negative"
	elif alc_neg_count < alc_pos_count:
		alc_sent_from_examples = "positive"
	else:
		alc_sent_from_examples = "neutral"
	print "Sentiment from examples: ", alc_sent_from_examples

	if alc_sent_score < 0:
		alc_sent_from_score = "negative"
	elif alc_sent_score > 0:
		alc_sent_from_score = "positive"
	else:
		alc_sent_from_score = "neutral"

	print "Sentiment from score: ", alc_sent_from_score 

	# return(alc_pos_count, alc_neg_count, pos_examples, neg_examples, pos_percent, neg_percent)
	return (alc_pos_count, alc_neg_count, pos_percent, neg_percent)


# def main():

# 	sent_system(test, text_to_info, topic)

# if __name__ == '__main__':
#     main()






