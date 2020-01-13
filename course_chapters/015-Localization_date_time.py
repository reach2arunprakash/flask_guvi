#pip install flask-moment

from flask_moment import Moment
from datetime import datetime

moment= Moment(guvi_app)  

@guvi_app.route('/')
def index():
	return render_template('local_date.html', current_time=datetime.utcnow())