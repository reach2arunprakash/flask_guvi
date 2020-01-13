#pip install flask-mysql

from flask import Flask
from flaskext.mysql import MySQL
 
mysql = MySQL()
app_guvi = Flask(__name__)
app_guvi.config['MYSQL_DATABASE_USER'] = 'root'
app_guvi.config['MYSQL_DATABASE_PASSWORD'] = ''
app_guvi.config['MYSQL_DATABASE_DB'] = 'sms'
app_guvi.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app_guvi)


@app_guvi.route("/")
def hello():
	cursor = mysql.connect().cursor()
	return "Connected successfully"

if __name__ == "__main__":
    app_guvi.run()
