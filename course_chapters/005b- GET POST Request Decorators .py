#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

#http://127.0.0.1:5000/hi?username=arun&password=mypass&session=2

from flask import Flask, render_template, request ,redirect, url_for
from flask import flash


app_guvi = Flask(__name__)
app_guvi.secret_key = "super secret key"

@app_guvi.before_request
def before_reques():
	#active session check
	if request.args['auth_token'] == '1':
		print request.args['username'] + 'beforearray'
		print request.args.get('password') + 'before'
	else:
		flash("please login - ur auth token has expired")

	'''
@app_guvi.after_request
def before_reques():
	print request.args.get('username') + 'after'
	print request.args.get('password') + 'after'
'''	
def about():
	return "about page"
	
app_guvi.add_url_rule('/about', 'about', about)


@app_guvi.route('/hi',methods=['GET','POST'])
def hi_guvi():
	str = "Path:"+request.path + " Method:" + request.method
	username = request.args.get('username')
	password = request.args.get('password')
	return 'Hello from GUVI\n' + str + password + username
		

@app_guvi.route('/')
def index():
    return redirect(url_for('about'))

if __name__ == "__main__":
	app_guvi.run(debug = True)
	#app_guvi.run()

#curl -i -X POST http://127.0.0.1:5000/about
#curl -i -X POST http://127.0.0.1:5000/about