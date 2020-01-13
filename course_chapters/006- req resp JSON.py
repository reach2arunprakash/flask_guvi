#python "D:\Arun\GUVI\tryouts\Flask\001-hello world render template.py" runserver -d

from flask import Flask, render_template, request,Response
import json

app_guvi = Flask(__name__)

def about():
	return "about page"
	
app_guvi.add_url_rule('/about', 'about', about)

@app_guvi.route('/sayhello',methods=['GET','POST'])
def index_guvi():
	data = {
        'hello'  : 'world',
        'number' : 3
		}
	js = json.dumps(data)
	print (js)
	resp = Response(js, status=200, mimetype='application/json')
	return resp



if __name__ == "__main__":
	app_guvi.run(debug = True)
	#app_guvi.run()
	