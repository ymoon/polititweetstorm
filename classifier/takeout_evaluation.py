import pandas
#from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json
import math

#deals with decoding errors
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

input = "sad.csv"

#dictionary mapping the number of positive tweets that appear in data and the number of negative tweets
#eg. {positive: 4992000, negative: 423482340203}
class_probs ={}
#dictionary mapping the size (i.e. how many words (not unique) per positive and negative)
#eg. {positive: 209348209348129348, negative: 2039482093481234}
cateogry_size = {}
#dictionary mapping the frequency of the word given the sentiment
#eg {positive: {hey: 4, how: 5, is: 6, your_mom: 80000, negative: {lolz: 234}}
word_probs = {}

#list containing test sentences and sentiment as tuples - sentiment will be used for evaluation
#eg [("hey how is your_mom lolz", "positive"), ("get outta here boyyyy", "negative")]
test_tweets = []


test_num = 0;
total_test_count = 0;
round_number = 1;
max_test_count = 100000 #total number of docs to eventually use as test data
takeout_amount = 1000 # how much we want to pull out at at time to use as a test (traditionally 1 but might be too ineeficient)

correct_prediction_count = 0 #used to store number of classification that were correctly classified

#1). Loop through data to get tweets - grab chunk for testing 
while ((round_number * takeout_amount) < max_test_count):
    for df in pandas.read_csv(input, chunksize=1):
        if(test_num in range(total_test_count, (takeout_amount * round_number))):
            #store this chunk for testing
            sent_int = int(df.iloc[0]['Sentiment'])#0 is negative, 1 is postive
            if sent_int == 0:
                sent = 'neg'
            else:
                sent = 'pos'
            test_tweets.append((str(df.iloc[0]['SentimentText']), sent))

        else: #not in the test set so use for training
            sent_int = int(df.iloc[0]['Sentiment'])#0 is negative, 1 is postive
            if sent_int == 0:
                sent = 'neg'
            else:
                sent = 'pos'
            
            class_probs[sent] = class_probs.get(sent, 0) + 1#add to class frequency dictionary
            
            text = str(df.iloc[0]['SentimentText']) #grabbing actual twitter text from the SentimentText column

            try:
                tokens = word_tokenize(text) #tokenize the tweet text
            except UnicodeDecodeError: #catch decode errors 
                continue

            cateogry_size[sent] = cateogry_size.get(sent, 0) + len(tokens) #add to total word count dictionary

            #for each token in your token list, add frequency to dictionary of word probs for that category
            for t in tokens:
                lower_t = t.lower()
                word_probs[sent] = word_probs.get(sent, {})
                word_probs[sent][t] = word_probs[sent].get(t, 0) + 1

        test_num += 1
        total_test_count += 1
    
    #do evaluation with current test tweets
    

    training = []

    training.append(class_probs)
    training.append(cateogry_size)
    training.append(word_probs)

    #positive and negative tweet counts specific to location and query that came in
    pos = 0
    neg = 0

    #parse dictionaries from training
    class_probs = training[0]
    cateogry_size = training[1]
    
    word_probs = training[2]

    #lists of example texts
    pos_examples = []
    neg_examples = []

    #total number of tweets classified from training
    total_tweets = class_probs.get("neg", 0) + class_probs.get("pos", 0)

    #get intersection of tokens to get vocab size
    keys_neg = set(word_probs["neg"].keys())
    keys_post = set(word_probs["pos"].keys())
    vocab = keys_neg & keys_post
    vocab_size = len(vocab)

    
    #loop through test_tweets to classify each tweet in results
    for tweet in test_tweets:
        #dictionary to map positive and negative to their 
        #respective probabilites, the max of the two will be the sentiment
        sent_probs = {}

        try:
            tokens = word_tokenize(tweet[0])
        except UnicodeDecodeError:
            continue

        #essentialy do this twice: once for positive and once for negative
        for sentiment in class_probs:
            for to in tokens:
                t = to.lower()
                #sum of log (# of times word appears in pos/neg tweets +  1/ total words in pos/neg tweets + vocab size)
                sent_probs[sentiment] = sent_probs.get(sentiment, 0) + math.log(float(word_probs[sentiment].get(t, 0) + 1) /float((cateogry_size[sentiment]) + vocab_size))

        #add log of class probs with smoothing to previous sums
        for sentiment in class_probs:
            sent_probs[sentiment] += math.log(float(class_probs.get(sentiment, 0) + 1) / float(total_tweets + vocab_size - 1))

        # find which had the max probabiity (neg or pos)
        if sent_probs["neg"] > sent_probs["pos"]:
            max_sent = "neg"
        else:
            max_sent = "pos"

        if max_sent == tweet[1]:
            correct_prediction_count += 1


    #reset for next round of test tweets
    test_tweets = []
    test_num = 0
    round_number += 1

results = {}
results["predicted"] = correct_prediction_count
results["count"] = max_test_count
results["accuracy"] = float(correct_prediction_count)/float(max_test_count)

with open("to_eval_res.json", 'w') as ter:
    json.dump(results, ter)


print "Number of Correctly classified tweets is:", results["predicted"]
print "Total number of test tweets used:", results["count"]
print 'Accuracy of the system:', results["accuracy"]




