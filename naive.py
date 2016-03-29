import pandas
from nltk.classify import NaiveBayesClassifier as nbc
from nltk import FreqDist as fd



input = "sad.csv"

list = []
tokens = []
words = []
count = 0

#read row by row from csv file: http://thinknook.com/twitter-sentiment-analysis-training-corpus-dataset-2012-09-22/
for df in pandas.read_csv(input, chunksize=1):
    if(count > 11):
        break
    else:
        sent = str(df.iloc[0]['Sentiment']) #grabbing sentiment column value, 1 = pos 0 = neg
        text = str(df.iloc[0]['SentimentSource']) #grabbing actual twitter text from the SentimentSource column
        list = [t.lower() for t in text.split()] #list comprehension, tokenizing by spaces the text
        tokens.append((list, sent)) #creating a list of tuples with list of tokens, pos/neg
        words.extend(list) #create a list of just the words
        count +=1


frequency_dictionary = fd(words) #creates frequency distribution of all the words in all tweet
word_features = frequency_dictionary.keys() #creates list of word features ordered by frequency








