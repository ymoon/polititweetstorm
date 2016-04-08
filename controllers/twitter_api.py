from flask import *
from extensions import mysql


dani = "https://api.twitter.com/1.1/trends/place.json?id=1"
link = "https://api.twitter.com/1.1/search/tweets.json?q="
hashtag = "%23"
CONSUMER_KEY = "h2Ky8wu3DuBit9b86cgeuPNJd"
CONSUMER_SECRET = "7xP8Y4VA5WwH8anlIEZwlBKzu4N7bmRtfTa0EMu4jroKJePXfO"


twitter_api = Blueprint('twitter_api', __name__, template_folder='templates')

@twitter_api.route('/api/v1/twitter/<string:query>', methods=['GET'])
def twitter_api_route(query):
	return
	# if request.method == 'GET':