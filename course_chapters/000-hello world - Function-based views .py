from flask import Flask

app_guvi = Flask(__name__)

#,methods=['GET','POST']

@app_guvi.route('/',methods=['GET','POST'])
def index_guvi():
	return "hey how r u " + 1

@app_guvi.route('/IT',methods=['POST'])
def index_IT():
	return "hello IT"
	
@app_guvi.route('/CSE',methods=['GET','POST'])
def index_CSE():
	return "CSE"

if __name__ == "__main__":
    app_guvi.run(debug=True)
	
	#host='0.0.0.0', port=80
	#debug=true
	