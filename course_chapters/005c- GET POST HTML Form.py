#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request ,redirect, url_for
from werkzeug import generate_password_hash, check_password_hash

app_guvi = Flask(__name__)



@app_guvi.route('/signUp',methods=['POST'])
def signUp():
	strName = request.form['inputName'] 
	strEmail = request.form['inputEmail'] 
	strPwd = request.form['inputPassword']
	_hashed_password = generate_password_hash(strPwd)
	
	
	app_guvi.logger.debug(request.form['inputName'])
	app_guvi.logger.debug(request.form['inputEmail'])
	app_guvi.logger.debug(request.form['inputPassword'])
	
	#return strName +" "+ strEmail +" "+ strPwd
	return strName +" "+ strEmail +" "+ _hashed_password
		

@app_guvi.route('/')
def index():
    return render_template("signup.html")

if __name__ == "__main__":
	app_guvi.run(debug = True)
	#app_guvi.run()

#curl -i -X POST http://127.0.0.1:5000/about
#curl -i -X POST http://127.0.0.1:5000/about