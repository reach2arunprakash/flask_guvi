#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request ,redirect, url_for
from flask_cors import CORS


app_guvi = Flask(__name__)

CORS(app_guvi)
'''
def about():
	return "about page"
	
app_guvi.add_url_rule('/about1', 'about', about)
'''

@app_guvi.route('/hi')
def hi_guvi():
	str = "Path:"+request.path + " Method:" + request.method
	username = request.args.get('username')
	password = request.args.get('password')
	return 'Hello from GUVI\n' + str + "\n"+ password + username
		
'''
@app_guvi.route('/')
def index111():
    return redirect(url_for('about'))
'''
if __name__ == "__main__":
	app_guvi.run(debug = True)
	#app_guvi.run()

#curl -i -X POST http://127.0.0.1:5000/about
#curl -i -X POST http://127.0.0.1:5000/about