from flask import *
from extensions import mysql

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def main_route():
    # trending = get_trending_data()
    return render_template("index.html")

# def get_trending_data():
# 	cur = mysql.cursor()
# 	cur.execute('SELECT topic FROM polititweetstorm.Trending')
# 	trending = cur.fetchall()
# 	return trending