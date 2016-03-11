from flask import *
from extensions import mysql

link = "https://api.twitter.com/1.1/search/tweets.json?q="

twitter_api = Blueprint('twitter_api', __name__, template_folder='templates')

@twitter_api.route('/api/v1/twitter/<string:query>', methods=['GET'])
def twitter_api_route(query):
	if request.method == 'GET':


