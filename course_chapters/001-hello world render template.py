#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request

app_guvi = Flask(__name__)


@app_guvi.route('/',methods=['GET','POST'])
def index_guvi():
	#return "<html><body><h1>Hello World'</h1></body></html>"
	return render_template('index.html')


if __name__ == "__main__":
	#app_guvi.run(debug = True)
	app_guvi.run()
	