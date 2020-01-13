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
 
@app_guvi.route("/<uname>")
def hello(uname):
	username = uname
	password = 'sp12345'
	cursor = mysql.connect().cursor()
	cursor1 = mysql.connect().cursor()

	#cursor.execute("SELECT * from logins where Username='" + username + "' and Password='" + password + "'")
	cursor.execute("select table_name from information_schema.tables where table_schema='sms'");
	ret_data =""
	for row in cursor:
		cursor1.execute()
		ret_data += str(row)
	data = cursor.fetchone()
#	if data is None:
#		return "Username or Password is wrong"
#	else:
	return ret_data + "test"

 
if __name__ == "__main__":
    app_guvi.run()
