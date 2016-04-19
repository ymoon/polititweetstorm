from flask import Flask, render_template

# from extensions import mysql
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.main, url_prefix='/polititweetstorm', static_url_path="static")
app.register_blueprint(controllers.search, url_prefix='/polititweetstorm', static_url_path="static")

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    # change to host for server when submitting
    # app.run(host='eecs485-22.eecs.umich.edu', port=2600, debug=False)
    # app.run(host='eecs485-22.eecs.umich.edu', port=2601, debug=False)
    app.run(host='0.0.0.0', port=3000, debug=True)
