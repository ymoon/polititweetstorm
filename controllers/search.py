from flask import *
import classifier.get_tweets as gt
import classifier.naive_system as ns
import classifier.topic_search as ts
import googlemaps
# import classifier.naive_training as nt


search = Blueprint('search', __name__, template_folder='templates')

def get_geocor(city):



	gmaps = googlemaps.Client(key='AIzaSyCTNIg-6BKYrjrB9DnLij6tX4sAw_XeYrk')

# Geocoding an address
	geocode_result = gmaps.geocode(city)[0]
	lat = geocode_result['geometry']['location']['lat']
	lng = geocode_result['geometry']['location']['lng']
	return lat, lng


# def get_geocor(city):
@search.route('/search', methods=['GET', 'POST'])
def search_route():
	
	if request.method == "POST":
		text_to_json = {}
		topic = request.args.get("topic")
		location = request.args.get("location")
		relevent_tweets = set()
		if topic and location: #requests/search has been sent - run it and load the results page
			location = get_geocor(location) #get lat and lng of city
			search_results = gt.grab_tweets(topic, location)
			for x in search_results["statuses"]:
				sentance = x["text"]
				text_to_json[sentance] = x
				relevent_tweets.add(x)
			# if it is a bigram
			topic = topic.split()
			if len(topic) > 1:
				search_results2 = gt.grab_tweets(topic[0], location)
				for x in search_results2["statuses"]:
					sentance = x["text"]
					text_to_json[sentance] = x
					relevent_tweets.add(x)

				search_results3 = gt.grab_tweets(topic[1], location)
				for x in search_results3["statuses"]:
					sentance = x["text"]
					text_to_json[sentance] = x
					relevent_tweets.add(x)

				
			sentiment_results = ns.sent_system(relevent_tweets, text_to_json)
			return render_template("results.html", sentiment_results = sentiment_results)
	else: #the normal search page display trending topics
		topics = ts.get_top_topics()
	return render_template("search.html", initialize=True, topics = topics)

