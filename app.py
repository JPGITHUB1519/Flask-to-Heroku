from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *
app = Flask(__name__)
db = SQLAlchemy(app)
@app.route('/')
@app.route('/welcome')
def hello():
	posts = db.session.query(Post).all()
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)