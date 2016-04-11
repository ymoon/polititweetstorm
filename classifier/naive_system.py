from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json

#turn this file into classification function

def sent_system(search_results, text_to_json):

	#positive and negative tweet counts - specific to a location query that came in 
	pos = 0
	neg = 0

	# 4) Read from that file and store back into structure that it originally was 
			#- MAKE SURE STRUCTURE IS CORRECT
	with open("training_formatted_data.json", 'r') as tfd:
		training = json.load(tfd) 

	# 4) b. Read from the file from the training which has all feature words stored in a json object (list)
	with open("feature_words.json", 'r') as fw:
		the_words = json.load(fw)

	# # 4) c. Read from the query file assuming we save it in another file
	# with open("results.json", 'r') as q:
	# 	q_results = json.load(q)

	# 5) Pass that data into the classifier object - training the classifier
	nb_classifier = NBC.train(training)

	# 6) read api request results from file, parse text of tweets and save into test_sentence
	pos_examples = []
	neg_examples = []

	for tweet in search_results:
		#print test_sentence

	# 7) Grab the content of each tweet and format into testable data - like how we formatted training data
		#- NOT SURE WHAT TWEET DATA (test_sentences) WILL LOOK LIKE BUT LOOP THRU IT AND RUN THE FOLLOWING CODE TO FORMAT IT
		#collects every word mapped to whether or not it is in the test sentence
		test_sent_features = {word.lower(): (word in word_tokenize(tweet.lower())) for word in the_words}
		
		#within the loop

		#8) run classification on each tweet and receive its sentiment 
			#NEED TO SET UP tweet_id VALUE AND location VALUE
		if nb_classifier.classify(test_sent_features) == "pos":
			pos += 1
			if len(pos_examples) < 10:
				pos_examples.append(tweet)
		else:
			neg += 1
			if len(neg_examples) < 10:
				neg_examples.append(tweet)

	# creates a list for of json objects of tweets of negative and positive examples
	for x in pos_examples:
		x = text_to_json[x]

	for x in neg_examples:
		x = text_to_json[x]

			# 9) store the class and the tweets and whatever else - should all be in that dictionary
		#-don't actually need to do anything in this step since it is in dictionary
	# 10) determine the overall/average class of the tweets in that area

	return (pos, neg, pos_examples, neg_examples)

	#- !!! can just determine which class for location is better by doing comparison on the front end side or can do before hand !!!
	# 11) pass the location data dictionary to the front end to be displayed 
		#FILL THIS IN

