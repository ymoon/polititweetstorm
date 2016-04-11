from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json
import math

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

#search_results = , text_to_info = dictionary of text to (user, time)
def sent_system(search_results, text_to_info):

	#positive and negative tweet counts - specific to a location query that came in 
	pos = 0
	neg = 0
	
	with open("training_information.json", 'r') as ti:
		training = json.load(ti)


	#parse dictionaries from training
	class_probs = {}
	class_probs = training[0]
	cateogry_size = {}
	cateogry_size = training[1]
	word_probs = {}
	word_probs = training[2]


	# #testing:
	# print "hate freq neg: "
	# print word_probs["neg"]["hate"]
	# print cateogry_size["neg"]
	# print "hate freq pos: "
	# print word_probs["pos"]["hate"]
	# print cateogry_size["pos"]

	# print "class probs: "
	# for s in class_probs:
	# 	print s
	# print "cateogry_size: "
	# for s in cateogry_size:
	# 	print s
	# print "word_probs: "
	# for s in word_probs:
	# 	print s

	pos_examples = []
	neg_examples = []

	#total number of tweets classified from training
	total_tweets = class_probs.get("neg", 0) + class_probs.get("pos", 0)


	keys_neg = set(word_probs["neg"].keys())
	keys_post = set(word_probs["pos"].keys())
	vocab = keys_neg & keys_post
	vocab_size = len(vocab)

	#loop through search_results to classify each tweet
	for tweet in search_results:
		#print tweet
		#dictionary to map positive and negative to their 
		#respective probabilites, the max of the two will be the sentiment
		sent_probs = {} 

		try:
			tokens = word_tokenize(tweet) 
		except UnicodeDecodeError:
			continue

		#esentailly do this twice: once for positive and once for negative
		for sentiment in class_probs:
			for to in tokens:
				t = to.lower()
				#sum of log (# of times word appears in pos/neg tweets +  1/ total words in pos/neg tweets + vocab size)
				sent_probs[sentiment] = sent_probs.get(sentiment, 0) + math.log( float( word_probs[sentiment].get(t, 0) + 1 ) / float( cateogry_size[sentiment] + vocab_size))

		#add the log of the class prob (with smoothing) to the sum 
		for sentiment in class_probs:
			sent_probs[sentiment] += math.log(float(class_probs.get(sentiment, 0) + 1) / float(total_tweets + vocab_size - 1))

		#find the max prob between pos and neg
		max_v = float("-inf")
		max_sent = "test"
    	for sent in sent_probs:
    		if sent_probs[sent] > max_v:
    			max_v = sent_probs[sent]
    			max_sent = sent

    	#add to counts and add example tweets
    	if max_sent == "pos":
    		pos += 1
    		if len(pos_examples) < 10: #only want ten examples
    			pos_examples.append(tweet)
    	else:
    		neg += 1
    		if len(neg_examples) < 10: #only want ten exmaples
    			neg_examples.append(tweet)

	# creates a list for of json objects of tweets of negative and positive examples
	
	# for x in pos_examples:
	# 	x = text_to_info[x]

	# for x in neg_examples:
	# 	x = text_to_info[x]
	# print pos
	# print neg
	return (pos, neg, pos_examples, neg_examples)

#for testing purposes:
# def main():
# 	sent_system(test, "blob")


# if __name__ == '__main__':
#     main()