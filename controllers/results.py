from flask import *
import classifier.get_tweets as gt
import classifier.naive_system as ns
import classifier.topic_search as ts
# import classifier.naive_training as nt

results = Blueprint('results', __name__, template_folder='templates')

@results.route('/results')
def search_route():
	topics = ts.get_top_topics()
	return render_template("results.html", topics = topics)
