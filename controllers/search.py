from flask import *
import get_tweets as gt
import naive_system as ns
import topic_search as ts
import naive_training as nt


search = Blueprint('search', __name__, template_folder='templates')


@search.route('/search')
def search_route():

	if topic: #requests/search has been sent - run it and load the results page
		topic = request.args.get("topic")
		location = request.args.get("location")

		search_results = gt.grab_tweets(topic, location)
		sentiment_results = nt.sent_system(search_results)


		return render_template("results.html", sentiment_results = sentiment_results)
	else: #the normal search page
		#display trending topics
		topics = ts.get_top_topics()

		return render_template("search.html", topics = topics)
