from flask import *

dani = Blueprint('dani', __name__, template_folder='templates')

@dani.route('/dani')
def dani_route():
    return render_template("dani.html")