from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json


#positive and negative tweet counts - specific to a location query that came in 
pos = 0
neg = 0

# 4) Read from that file and store back into structure that it originally was 
		#- MAKE SURE STRUCTURE IS CORRECT
with open("training_formatted_data.json", 'r') as tfd:
	training = json.load(tfd) 

# 5) Pass that data into the classifier object - training the classifier
nb_classifier = NBC.train(training)

# 6) Run api request to get tweets form users containing our specified political words
	#- FILL THIS IN - MIGHT BE BEST TO READ THIS IN FROM A FILE AS WELL


# 7) Grab the content of each tweet and format into testable data - like how we formatted training data
	#- NOT SURE WHAT TWEET DATA (test_sentences) WILL LOOK LIKE BUT LOOP THRU IT AND RUN THE FOLLOWING CODE TO FORMAT IT
	the_words = #this needs to be the same set of words from before - FIGURE THIS OUT - file storage again?
	#collects every word mapped to whether or not it is in the test sentence
	test_sent_features = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
	
	#within the loop

	#8) run classification on each tweet and receive its sentiment 
		#NEED TO SET UP tweet_id VALUE AND location VALUE
	if nb_classifier.classify(test_sent_features) == "pos":
		pos += 1
	else:
		neg += 1


# 9) store the class and the tweets and whatever else - should all be in that dictionary
	#-don't actually need to do anything in this step since it is in dictionary
# 10) determine the overall/average class of the tweets in that area


#- !!! can just determine which class for location is better by doing comparison on the front end side or can do before hand !!!
# 11) pass the location data dictionary to the front end to be displayed 
	#FILL THIS IN

