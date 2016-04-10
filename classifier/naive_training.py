import pandas
#from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json

#deals with decoding errors
import sys
reload(sys)  
sys.setdefaultencoding('utf8')

input = "sad.csv"

tokens = []
words = []
count = 0
trainSentences = []

#1) read in data to eventually use as training

#read row by row from csv file: http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/
for df in pandas.read_csv(input, chunksize=1):
    if(count == -1):
        break
    else:
        sent = int(df.iloc[0]['Sentiment']) #grabbing sentiment column value, 1 = pos 0 = neg
        if sent == 0:
            sentString = 'neg'
        else:
            sentString = 'pos'
        text = str(df.iloc[0]['SentimentText']) #grabbing actual twitter text from the SentimentSource column
        trainSentences.append((text, sentString))
        count +=1

print "done with reading input"

# frequency_dictionary = fd(words) #creates frequency distribution of all the words in all tweet
# word_features = frequency_dictionary.keys() #creates list of word features ordered by frequency

# 2) turn data into the specified format to use as training data

#create a set from a generator
#generator takes each sentence and tokenizes it, lowercases it and puts it into a set
#result is every word in the training vocab
#the_words = list(set(word.lower() for s in trainSentences for word in word_tokenize(s[0])))

#to account for decode errors 
the_words = set([])

for s in trainSentences:
    try:
        tok_words = word_tokenize(s[0])
    except e:
        continue
    for word in tok_words:
        the_words.add(word.lower())

the_words = list(the_words)

print "done with creating the words"
#collects every word mapped to whether or not it is in the tokenized sentence and then if that sentence was set as pos or neg
#training = [({word : (word in word_tokenize(t[0])) for word in the_words}, t[1]) for t in trainSentences]

training = []

for t in trainSentences:
    dic = {}
    try:
        tok_sent = word_tokenize(t[0])
    except e:
        continue
    for word in the_words:
        if word in tok_sent:
            dic[word] = True
        else:
            dic[word] = False
    entry = (dic, t[1])
    training.append(entry)

print "done with mapping traning data"
#3) store the converted training data into a file
    #JSON easiest to store and re load
with open("training_formatted_data.json", 'w') as tfd:
    json.dump(training, tfd)

print "dumped training data"

#3.1) output features/words to a file
with open("feature_words.json", "w") as fw:
    json.dump(the_words, fw)

print "dumped featued words"




