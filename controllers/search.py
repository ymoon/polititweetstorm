from flask import *
import classifier.get_tweets as gt
import classifier.system as ns
import classifier.alc_system as alcS
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
		# Refresh topics by clearing the session
		if request.form.get("op") == "topic_refresh":
			session.clear()
			print "session cleared"
			return redirect(url_for('search.search_route'))
		else:
			text_to_info = {}
			topic = request.form.get("topic")
			orig_topic = topic
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

			if request.form.get("action") == "Submit":
				print "entered submit reg"
				sentiment_results = ns.sent_system(relevent_tweets, text_to_info)
				return render_template("results.html", sentiment_results=sentiment_results, topic=topic, location=location_name)
			elif request.form.get("action") == "AlchemySubmit":
				print "entered submit alchemy"
				alc_sentiment_results = alcS.alc_sent_system(relevent_tweets, text_to_info, orig_topic)
				entity = alc_sentiment_results[-1]
				return render_template("alchemyresults.html", sentiment_results=alc_sentiment_results[:-1], topic=entity, location=location_name)
	else: # Display trending topics - The normal search page 
		# Check if topics have been stored in cookies/already retrieved for the day
		if 'topics' not in session:
			print "retrieving topics"
			topics = ts.get_top_topics()
			session['topics'] = topics
		else:
			print "session active"
			topics = session['topics']
		return render_template("search.html", initialize=True, topics=topics)

