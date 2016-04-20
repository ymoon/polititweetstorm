from nltk.tokenize import word_tokenize
import nltk
import json
import math
import pandas

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def sent_system():
    count = 0
    with open("training_information1000.json", 'r') as ti:
        training = json.load(ti)

    # parse dictionaries from training
    class_probs = {}
    class_probs = training[0]
    cateogry_size = {}
    cateogry_size = training[1]
    word_probs = {}
    word_probs = training[2]

    total_tweets = class_probs.get("neg", 0) + class_probs.get("pos", 0)

    keys_neg = set(word_probs["neg"].keys())
    keys_post = set(word_probs["pos"].keys())
    vocab = keys_neg & keys_post
    vocab_size = len(vocab)
    total = 1000  # total number of tweets we are testing
    correct = 0

    input = "sad.csv"
    for df in pandas.read_csv(input, chunksize=1):

        count += 1
        print count

        if (count > 1000):
            break
        else:

            sent_int = int(df.iloc[0]['Sentiment'])  # 0 is negative, 1 is postive
            if sent_int == 0:
                acutal_sent = 'neg'
            else:
                acutal_sent = 'pos'

                # positive and negative tweet counts specific to location and query that came in

            # dictionary to map positive and negative to their
            # respective probabilites, the max of the two will be the sentiment
            sent_probs = {}

            text = str(df.iloc[0]['SentimentText'])

            try:
                tokens = word_tokenize(text)
            except UnicodeDecodeError:
                continue

            ##esentailly do this twice: once for positive and once for negative
            for sentiment in class_probs:
                for to in tokens:
                    t = to.lower()
                    # sum of log (# of times word appears in pos/neg tweets +  1/ total words in pos/neg tweets + vocab size)
                    sent_probs[sentiment] = sent_probs.get(sentiment, 0) + math.log(
                        float(word_probs[sentiment].get(t, 0) + 1) / float((cateogry_size[sentiment]) + vocab_size))

            # add log of class probs with smoothing to previous sums
            for sentiment in class_probs:
                sent_probs[sentiment] += math.log(
                    float(class_probs.get(sentiment, 0) + 1) / float(total_tweets + vocab_size - 1))

            # find which had the max probabiity (neg or pos)
            if sent_probs["neg"] > sent_probs["pos"]:
                max_sent = "neg"
            else:
                max_sent = "pos"

            if max_sent == acutal_sent:
                correct += 1

    return (correct, total)


print sent_system()
