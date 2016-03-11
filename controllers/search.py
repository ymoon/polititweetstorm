from flask import *

search = Blueprint('search', __name__, template_folder='templates')

@search.route('/search/edit')
def search_edit_route():
	options = {
		"edit": True
	}
	return render_template("search.html", **options)

@search.route('/search')
def search_route():
	options = {
		"edit": False
	}
	return render_template("search.html", **options)
