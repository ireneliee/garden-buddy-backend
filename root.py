from flask import Flask
from flask import render_template

flask_app = Flask(__name__, static_url_path='/static')

@flask_app.route('/')
def index():
	return render_template('index.html', title = "Garden Buddy Homepage", content = "I love Garden Buddy")
