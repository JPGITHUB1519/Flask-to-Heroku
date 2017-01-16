from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/welcome')
def hello():
	return "Welcome To Flask"

if __name__ == "__main__":
	app.run()