#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request

app_guvi = Flask(__name__)


@app_guvi.route('/',methods=['GET','POST'])
def index_guvi():
	dict = {'phy':50,'che':30,'maths':80}
	return render_template('index1.html', result = dict)


if __name__ == "__main__":
	app_guvi.run(debug = True)	