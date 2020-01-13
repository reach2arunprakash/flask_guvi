#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request

app_guvi = Flask(__name__)


@app_guvi.route('/')
def index_guvi():
	return render_template('index.html')


if __name__ == "__main__":
	app_guvi.run()
	