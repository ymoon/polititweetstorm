from nltk.tokenize import word_tokenize
import nltk
import json
import math

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

# search_results: set of tweets that were returned from the relevant query
# text_to_info: maps the tweet to a tuple of information regarding that tweet (tweet, created, user)

# Function to calculate and return the overall sentement of the parsed tweets for the relevant query
def sent_system(search_results, text_to_info):

	# Positive and Negative tweet counts specific to location and query that came in
	pos = 0
	neg = 0

	with open("classifier/training_information.json", 'r') as ti:
		training = json.load(ti)

	# Parse dictionaries from training
	class_probs = {}
	class_probs = training[0]
	cateogry_size = {}
	cateogry_size = training[1]
	word_probs = {}
	word_probs = training[2]

	# Lists of example texts
	pos_examples = []
	neg_examples = []

	# Total number of tweets classified from training
	total_tweets = class_probs.get("neg", 0) + class_probs.get("pos", 0)

	keys_neg = set(word_probs["neg"].keys())
	keys_post = set(word_probs["pos"].keys())
	vocab = keys_neg & keys_post
	vocab_size = len(vocab)


	# Loop through search_results to classify each tweet in results
	for tweet in search_results:


	# Loop through search_results to classify each tweet in results
	for tweet in search_results:
		
		# BELOW IS OLD SYSTEM - FOR NOW RUN BOTH

		# Dictionary to map positive and negative to their 
			# respective probabilites, the max of the two will be the sentiment
		sent_probs = {}


		try:
			tokens = word_tokenize(tweet)
		except UnicodeDecodeError:
			continue

		# Essentially do this twice: once for positive and once for negative
		for sentiment in class_probs:
			for to in tokens:
				t = to.lower()
				# Sum of log (# of times word appears in pos/neg tweets +  1/ total words in pos/neg tweets + vocab size)
				sent_probs[sentiment] = sent_probs.get(sentiment, 0) + math.log(float(word_probs[sentiment].get(t, 0) + 1) /float((cateogry_size[sentiment]) + vocab_size))

		# Add log of class probabilities with smoothing to previous sums
		for sentiment in class_probs:
			sent_probs[sentiment] += math.log(float(class_probs.get(sentiment, 0) + 1) / float(total_tweets + vocab_size - 1))

		# Find which had the max probabiity (neg or pos)
		if sent_probs["neg"] > sent_probs["pos"]:
			max_sent = "neg"
		else:
			max_sent = "pos"

		if max_sent == "pos":
			pos += 1
			if len(pos_examples) < 10:
				pos_examples.append(tweet)
		else:
			neg += 1
			if len(neg_examples) < 10:
				neg_examples.append(tweet)


	# Creates a list for of json objects of tweets of negative and positive examples
	for i in range(len(pos_examples)):
		pos_examples[i] = text_to_info[pos_examples[i]]
	for i in range(len(neg_examples)):
		neg_examples[i] = text_to_info[neg_examples[i]]

	print pos
	print pos_examples
	print neg
	print neg_examples

	# print pos
	# print pos_examples
	# print neg
	# print neg_examples

	if (pos + neg > 0):
		pos_percent = (pos/float(pos+neg)) * 100
		neg_percent = (neg/float(pos+neg)) * 100
	else:
		print "Something went wrong/no tweets were found"
		pos_percent = 0
		neg_percent = 0

	print pos_percent
	print neg_percent

	# print pos_percent
	# print neg_percent


	return(pos, neg, pos_examples, neg_examples, pos_percent, neg_percent)


# def main():
# 	sent_system(test, text_to_info)

# if __name__ == '__main__':
#     main()






