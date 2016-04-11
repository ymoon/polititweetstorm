from nltk.classify import NaiveBayesClassifier as NBC
from nltk import FreqDist as fd
from nltk.tokenize import word_tokenize
import nltk
import json
import math

import sys
reload(sys)  
sys.setdefaultencoding('utf8')

# test = []
# test = [u'"Sanders camp girds itself in anticipation of revelations from Panama Papers"', u"DC Council passes bill to guarantee Bernie Sanders' place on DC primary ballot https://t.co/lLVdIgIqDU", u'Get Off My Lawn, Naive Bernie Kids (and Simple adult #BernieBros)! Why I\u2019m Voting for Hillary Clinton... https://t.co/TxVzvTfCbD #ImWithHer', u"@DWStweets \nHello,  \nPlease don't allow Bernie Sanders to disrupt the national convention in July.  Once Hillary has the delegates, she wins", u"RT @Joseph_Santoro: Dear Bernie: I Still Like You (less &amp; less), But These Red Flags Are Too Frequent to Ignore. It's time for you to go ht\u2026", u'@sgrant525 \nHi.  Love the picture of an angry Bernie.  Seems like all he knows is anger.  Hillary 2016!', u"@Earllangit @MariaTCardona \nI agree.  Sanders is under pressure and can't handle it. Unprepared!", u'The Pathetic #Sanders Campaign\u2019s #Sexist New Argument: #Hillary Tries Too Hard! https://t.co/SmgxLnvKVs #sexism #BernieSanders', u"Bernie Sanders' Ridiculous Charge Against Obama - it's racist dog whistle politics... Funny how #BernieBrosSoWhite. https://t.co/JiaKH836O3", u"TOXIC: The #Culture of #Bernie's Vile Campaign of Lies &amp; Hate! Witness the sewage that is #BernieSanders! https://t.co/21bSm29LYx", u'DC Council votes to allow Bernie Sanders on primary ballot after late registration https://t.co/BsT7o0GrCe', u'RT @WashingtonCP: Bernie Sanders supporters protest Hillary Clinton in Baltimore ---&gt; https://t.co/fHNaLl0GMs', u'Donald Trump contradicts himself on nuclear weapons \u2013 as it happened\nhttps://t.co/3oiPMihD66', u'#washingtondc #usa #election2016 hillaryclinton sanders @realdonaldtrump sentedcruz #travel @\u2026 https://t.co/fqxCR3F955', u"5) But Lombardi didn't coin the phrase, it was Red Sanders, &amp; it was 1st uttered publicly by young actress in John Wayne movie...", u'RT @samhusseini: "Revolution" \u201c@thenation: Both Clinton and Sanders are Qualified\u2014But Only Sanders Calls for Political Revolution https://t\u2026', u"@jaketapper \nYou're such a tool for Sanders.  It's pathetic!", u'RT @samhusseini: In NPR interview re Wisconsin, guest starts talking about Sanders message on trade resonating, interviewer redirects convo\u2026', u"@kwelkernbc \nWhy don't you go and work on the Sanders campaign? You push Sanders at every turn.  I would hope that the Clinton campaign", u'NEA #Jazz masters Jason Moran, Gary Burton, David Murray, Pharoah Sanders, Jimmy Heath and\u2026 https://t.co/kmnf4ebMW9', u"@jaketapper \nNow that I know you're a hyper-liberal,  it makes so much sense why you hate Hillary so much.  Your love for Bernie shows.", u'Cruz and Sanders win! #2016', u"@allinwithchris \nYou know quite well that the head to head numbers make no difference now.  Why?  Because Sanders hadn't been tested yet.", u"@MariaTCardona\nHi,  I'm so disappointed in you. How could you not mention that Bernie hasn't been tested by the Republicans' fire squad?", u'"@mostawesomeblog: Bernie\'s a REAL New Yorker! Hillary is just a cheap imitation. https://t.co/gZ1Qym3cJV" Good that the VT primary is over', u"@tvkatesnow \nOf course you are welcoming Eric Garner's daughter.  Sanders in the person you're backing.  You're not objective.  Not at all.", u'@VanJones68 @CNN \nYou have picked a candidate.  You chose Sanders.  You can keep him!', u'@AlexWitt \nDemocrats will nominate Hillary Clinton,  despite what you Republicans in the news media do to push Sanders.  She win general.', u'RT @Joseph_Santoro: STUMPED: Bernie Admits Not Thinking Through How to Break up Big Banks...The only thing more clueless is a #BernieBro ht\u2026', u"@kristendahlgren \nYour bias reporting is noted. You can love Sanders and hate Hillary.  Just don't do it on air.  Thank you.", u'Bernie--max leverage time: HRC support for Glass-Steagall/mega-bank bust up for exit', u'"Revolution" \u201c@thenation: Both Clinton and Sanders are Qualified\u2014But Only Sanders Calls for Political Revolution https://t.co/fUqXfOAJt8\u201d', u'DECISION 2016: Bernie Sanders wins Democratic caucus in Wyoming, NBC News projects. https://t.co/6Bhnb4Y2vt', u'RT @drtyronegray20: @JuanMaBenitez \nYour support for Bernie Sanders is evident.  New York is Hillary country!', u"RT @drtyronegray20: @Kermet_Merl_Key @MariaTCardona @CNNTonight @donlemon \nYou don't understand pledge delegates. Bernie will not be the no\u2026", u"Clinton: 'I am so sick of the Sanders campaign lying about me'! Bernie's Trump-Style thuggish campaign MUST END! https://t.co/kp5Anb7RiG", u'@StephanieDube \nSorry,  the closed primary will stand.  Let Democrats vote for Democrats.  Hillary is a democrat and Sanders is a socialist.', u'Bernie Sanders Is Right: Black People ARE\xa0Poor https://t.co/ezksXk72jv https://t.co/xQZGf85Soe', u'Bernie Sanders supporters protest Hillary Clinton in Baltimore ---&gt; https://t.co/fHNaLl0GMs', u"Decision2016: GOP Ted Cruz and Democrat Bernie Sanders are angling for victories in today's Wisconsin primaries https://t.co/9D98eRBKPg", u'US Senate effort to rein in corporate greed of Airlines every more cramped airplane seats fails! Where was Sanders? https://t.co/hivG57w7xF', u"@sluggahjells \nToo bad your support won't help Bernie when he's watching Hillary get the nomination. Clinton 2016!", u"@AlexWitt \nYou're good, but not good enough.  I noticed that you didn't ask Nina about the Sanders' campaign first position on superdelegate", u"@MadisonSiriusXM \nBest standard bearer for the Democrats. She is a Democrat, and she understands her own policies.  Bernie doesn't.", u'The Pope invites #Sanders to the Vatican https://t.co/dsbjYSxSNQ', u'Cruz and Sanders both won in Colorado, but did they make up ground on the frontrunners? By the numbers. https://t.co/WzbPrzYJPT', u'Happy Birthday to my big sis Bernie!! @ Beechtree Homes https://t.co/sZtuWJIEtU', u"@SaculSacul \nInterested in Sanders winning NY?  They can't beat him.  They will help the candidate that's the weakest and can't win the", u"@Kermet_Merl_Key @MariaTCardona @CNNTonight @donlemon \nYou don't understand pledge delegates. Bernie will not be the nominee. Get over it!", u"@MariaTCardona @CNNTonight @donlemon \nYou didn't mention how Bernie hasn't been tested by Republicans' firing squad.  The numbers are wrong", u"RT @davidmaraniss: 5) But Lombardi didn't coin the phrase, it was Red Sanders, &amp; it was 1st uttered publicly by young actress in John Wayne\u2026", u'@MadisonSiriusXM \nI like you,  How,  but Bernie has no chance for this nomination and supporting him keeps his hopes up.  Hillary is the', u'#NeverForget how horrible a person #Sanders actually is! TRANSCRIPT: #BernieSanders meets with News Editorial Board https://t.co/QJud6GbN2r', u'@frate\nYour subjectivity in the Hillary v. Bernie race is very telling.  Your laughter with Ashley at the end of your piece was terrible.', u'@kwelkernbc \nThrows you off their plane and tells Sanders to pick you up.', u"DARTH BERNIE BACKLASH: I've Never Seen Hillary's Supporters This Fired Up... #BernieSanders has gone FULL TRUMP https://t.co/JW8sozBVXu #p2", u"@SaculSacul \nHi.  Just saw Sanders' campaign worker on Fox News saying how they will win NY.  Now,  tell me why Republicans at Fox News are", u"Wood Flooring Sanders &amp; Finishers - Weyer's Floor Service: (#Odenton, MD) https://t.co/0JDkLNcwVl #CustomerService #Job #Jobs #Hiring", u'RT @Joseph_Santoro: Get Off My Lawn, Naive Bernie Kids (and Simple adult #BernieBros)! Why I\u2019m Voting for Hillary Clinton... https://t.co/T\u2026', u'Drawn by:jaxdrawingsandmore @ Bernie Sanders for President https://t.co/NSdtHOzHoe', u'Bernie Sanders Is Even Less Competitive Than He Appears! #Losah! https://t.co/owHmDA39bZ #p2 #HillarySoQualified', u'@AlexWitt \nAnd others like Joe Scarborough and Willie etc will do all you can to help push Bernie Sanders on the scene with good praise.', u"@nikawright95\nSanders hadn't been put under any heavy combat from Republican. Surely you know that once that happens, his poll numbers drop!", u'@JuanMaBenitez \nYour support for Bernie Sanders is evident.  New York is Hillary country!', u"@AlexWitt \nThe Sanders' campaign first position was delegates should count and not superdelegates. But we know what's happening here. You", u'D.C. lawmakers will take up legislation intended to ensure that Bernie Sanders will be on the ballot ---&gt; https://t.co/BD0dp3uh90', u'RT @Joseph_Santoro: Why #Hillary\u2019s Visible Anger at Being Smeared Spells Big Trouble for #Bernie! https://t.co/ZgG8sZOpzd #FeelTheBern #ImW\u2026', u"@BryanLlenas \nYour pushing the socialist will not work.  Fox sees Sanders as the easier person to beat.  Democrats know this.  He won't be", u'RT @paulfuhlir: "@mostawesomeblog: Bernie\'s a REAL New Yorker! Hillary is just a cheap imitation. https://t.co/gZ1Qym3cJV" Good that the VT\u2026', u'@JoeNBC \nYou,  Willie,  and other Republicans are very good in promoting Bernie Sanders, who has no chance in winning a national election.', u"Dear Bernie: I Still Like You (less &amp; less), But These Red Flags Are Too Frequent to Ignore. It's time for you to go https://t.co/dsF16anWVS", u'@jdickerson \nYour biased coverage for Bernie Sanders will be of no account when she wins NY and gets the nomination.  Clinton 2016!!!!!!', u'DECISION 2016: NBC News projects Bernie Sanders will win the Wisconsin Dem. primary. @nbcwashington https://t.co/Z3EVsxwDWV', u"@aseitzwald \nBut I didn't see an article about how clueless Sanders was when confronted by the editorial board on his policies.  You all", u'Sanders...Over the Edge! Only YOU can prevent dumb kids from electing a Communist who makes the Left look THIS bad! https://t.co/ROrsuTwlLT', u'STUMPED: Bernie Admits Not Thinking Through How to Break up Big Banks...The only thing more clueless is a #BernieBro https://t.co/mzoidgj9rL', u"@nikawright95 \nSorry,  but you're wrong. Bernie doesn't beat many people in a head to head.  Surely a woman of your intelligence knows that", u"1 in 4 Sanders supporters won't vote for Clinton...THIS is why those of us in the know treat #BernieBros like kids https://t.co/16H9BF1bCN", u'Why #Hillary\u2019s Visible Anger at Being Smeared Spells Big Trouble for #Bernie! https://t.co/ZgG8sZOpzd #FeelTheBern #ImWithHer via @peterdaou', u'RT @Joseph_Santoro: Bernie Sanders Is Even Less Competitive Than He Appears! #Losah! https://t.co/owHmDA39bZ #p2 #HillarySoQualified', u'In NPR interview re Wisconsin, guest starts talking about Sanders message on trade resonating, interviewer redirects convo to Trump.', u'"Vote Bernie Sanders For President" #blinddogboutique #blinddog #vote #berniesanders\u2026 https://t.co/Ke475HvDyD', u'Bottom Line...Plain &amp; Simple...Hillary Clinton was a more effective lawmaker than Bernie Sanders! Why #ImWithHer! https://t.co/Yob5cjrzfi', u"Join the Weyer's Floor Service team! See our latest #CustomerService #job opening here: https://t.co/QIb3kh4V1T #Odenton, MD #Hiring", u'How dare you compare Hillary to Tracy Flick. https://t.co/BcpseFFsAD']
# text_to_info = "yay"

def sent_system(search_results, text_to_info):

	#positive and negative tweet counts specific to location and query that came in
	pos = 0
	neg = 0

	with open("classifier/training_information.json", 'r') as ti:
		training = json.load(ti)

	#parse dictionaries from training
	class_probs = {}
	class_probs = training[0]
	cateogry_size = {}
	cateogry_size = training[1]
	word_probs = {}
	word_probs = training[2]

	#lists of example texts
	pos_examples = []
	neg_examples = []

	#total number of tweets classified from training
	total_tweets = class_probs.get("neg", 0) + class_probs.get("pos", 0)

	keys_neg = set(word_probs["neg"].keys())
	keys_post = set(word_probs["pos"].keys())
	vocab = keys_neg & keys_post
	vocab_size = len(vocab)

	#loop through search_results to classify each tweet in results
	for tweet in search_results:
		#dictionary to map positive and negative to their 
		#respective probabilites, the max of the two will be the sentiment
		sent_probs = {}


		try:
			tokens = word_tokenize(tweet)
		except UnicodeDecodeError:
			continue

		##esentailly do this twice: once for positive and once for negative
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

		if max_sent == "pos":
			pos += 1
			if len(pos_examples) < 10:
				pos_examples.append(tweet)
		else:
			neg += 1
			if len(neg_examples) < 10:
				neg_examples.append(tweet)


	#creates a list for of json objects of tweets of negative and positive examples
	for x in pos_examples:
		x = text_to_info[x]
	for x in neg_examples:
		x = text_to_info[x]

	# print pos
	# print neg

	return(pos, neg, pos_examples, neg_examples)


# def main():
# 	sent_system(test, text_to_info)

# if __name__ == '__main__':
#     main()






