from flask import Flask,render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'GUVI'
socketio  = SocketIO(app)

@app.route("/")
def sessions():
	return render_template("sesssion.html")

def messageRecieved(methods=["GET","POST"]):
	print("messageRecieved")
	
@socketio.on("my_event")
def handel_my_custom_event(json,methods=["GET","POST"]):
			print("handel_my_custom_event"+str(json))
			socketio.emit("my response",json,callback=messageRecieved)
if __name__ == '__main__':
	socketio.run(app, debug=True)
	