from flask import *
import classifier.get_tweets as gt
import classifier.system as ns
<<<<<<< HEAD
=======
import classifier.alc_system as alcS
>>>>>>> alchemyIBMTest
import classifier.topic_search as ts
import googlemaps
import json


search = Blueprint('search', __name__, template_folder='templates')

# Function for geocoding a location
def get_geocor(city):
	gmaps = googlemaps.Client(key='AIzaSyCTNIg-6BKYrjrB9DnLij6tX4sAw_XeYrk')

	# Geocoding an address
	geocode_result = gmaps.geocode(city)[0]
	lat = geocode_result['geometry']['location']['lat']
	lng = geocode_result['geometry']['location']['lng']
	return lat, lng


@search.route('/search', methods=['GET', 'POST'])
def search_route():
	
	if request.method == "POST":
		print "test"
		text_to_info = {}
		topic = request.form.get("topic")
		location_name = request.form.get("location")
		print location_name
		print topic
		relevent_tweets = set()
		if topic and location_name: # Requests/search has been sent - run it and load the results page
			location = get_geocor(location_name) # Get latitude and longitude of city
			print location
			search_results = gt.grab_tweets(topic, location)
			for x in search_results["statuses"]:
				sentence = x["text"]
				text_to_info[sentence] = (sentence, x["created_at"], x["user"]["screen_name"])
				relevent_tweets.add(sentence)
			# if it is a bigram
			topic = topic.split()
			if len(topic) > 1:
				search_results2 = gt.grab_tweets(topic[0], location)
				for x in search_results2["statuses"]:
					sentence = x["text"]
					text_to_info[sentence] = (sentence, x["created_at"], x["user"]["screen_name"])
					relevent_tweets.add(sentence)

				search_results3 = gt.grab_tweets(topic[1], location)
				for x in search_results3["statuses"]:
					sentence = x["text"]
					text_to_info[sentence] = (sentence, x["created_at"], x["user"]["screen_name"])
					relevent_tweets.add(sentence)

		sentiment_results = ns.sent_system(relevent_tweets, text_to_info)
<<<<<<< HEAD
=======
		alc_sentiment_results = alcS.alc_sent_system(relevent_tweets, text_to_info, topic)
>>>>>>> alchemyIBMTest
		
		return render_template("results.html", sentiment_results = sentiment_results, topic = topic, location = location_name)
	else: # Display trending topics - The normal search page 
		topics = ts.get_top_topics()
		return render_template("search.html", initialize=True, topics = topics)

