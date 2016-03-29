import pandas
from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk



input = "sad.csv"

list = []
tokens = []
words = []
count = 0
trainSentences = []

#read row by row from csv file: http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/
for df in pandas.read_csv(input, chunksize=1):
    if(count > 11):
        break
    else:
        sent = str(df.iloc[0]['Sentiment']) #grabbing sentiment column value, 1 = pos 0 = neg
        if sent = 0:
            sentString = 'neg'
        else:
            sentString = 'pos'
        text = str(df.iloc[0]['SentimentSource']) #grabbing actual twitter text from the SentimentSource column
        # list = [t.lower() for t in text.split()] #list comprehension, tokenizing by spaces the text
        # tokens.append((list, sent)) #creating a list of tuples with list of tokens, pos/neg
        # words.extend(list) #create a list of just the words
        trainSentences.append((text, sentString))
        count +=1


# frequency_dictionary = fd(words) #creates frequency distribution of all the words in all tweet
# word_features = frequency_dictionary.keys() #creates list of word features ordered by frequency

#create a set from a generator
#generator takes each sentence and tokenizes it, lowercases it and puts it into a set
#result is every word in the training vocab
the_words = set(word.lower() for s in trainSentences for word in word_tokenize(s[0]))

#collects every word mapped to whether or not it is in the tokenized sentence and then if that sentence was set as pos or neg
training = [({word : (word in word_tokenize(t[0])) for word in the_words}, t[1]) for t in trainSentences]

nbClassifier = NBC.train(training)








