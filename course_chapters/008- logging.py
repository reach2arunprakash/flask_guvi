from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
	app.logger.debug('A value for debugging')
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.logger.error('An error occurred')
	return "hi i have logged"


if __name__ == "__main__":
	app.run(debug = True)
	#app_guvi.run()
	