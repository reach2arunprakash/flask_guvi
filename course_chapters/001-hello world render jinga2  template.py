#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request

app_guvi = Flask(__name__)

@app_guvi.route('/',methods=['GET','POST'])
def index_guvi1():
	return "simple fix"

@app_guvi.route('/student_details/<uname>',methods=['GET','POST'])
def index_guvi(uname):
	return render_template('index.html', uname = uname)


if __name__ == "__main__":
	app_guvi.run(debug = True)
	