from flask import Blueprint , render_template , request , Flask
from flask_mail import Mail , Message
import os

views = Blueprint('views' , __name__)

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vzlatev7@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@views.route('/' , methods = ["POST" , "GET"])

def home():
   
    if request.method == 'POST':
        msg = Message ('Hey' , sender = 'viktor.r.zlatev.2021@elsys-bg.org',
                      recipients=['vzlatev7@gmail.com'])
        msg.body = "hey how are you"
        mail.send(msg)
        return "Sent email"
    
    return render_template("base.html")
