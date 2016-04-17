import pandas
#from nltk.classify import NaiveBayesClassifier as NBC

from nltk.tokenize import word_tokenize
import nltk
import json

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


count = 0;

#1). Loop through training data to get tweets and their sentiments
for df in pandas.read_csv(input, chunksize=1):
    count += 1
    print count
    if(count == -1):
        break
    else:
        
        sent_int = int(df.iloc[0]['Sentiment'])#0 is negative, 1 is postive
        if sent_int == 0:
            sent = 'neg'
        else:
            sent = 'pos'
        
        class_probs[sent] = class_probs.get(sent, 0) + 1#add to class frequency dictionary
        
        text = str(df.iloc[0]['SentimentText']) #grabbing actual twitter text from the SentimentSource column

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



dictionaries = []

dictionaries.append(class_probs)
dictionaries.append(cateogry_size)
dictionaries.append(word_probs)


with open("training_informationNEW.json", 'w') as train:
    json.dump(dictionaries, train)

