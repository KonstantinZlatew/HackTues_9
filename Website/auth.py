from flask import Blueprint , render_template , request , redirect , url_for ,session
from .models import User
from werkzeug.security import generate_password_hash , check_password_hash
from . import db
from flask_login import login_user , login_required , logout_user , current_user
import time
import pyotp
import qrcode

auth = Blueprint('auth' , __name__)

@auth.route('/login' ,  methods = ["POST" , "GET"])
def login():
    if request.method == 'POST':
        
        email = request.form.get('email')
        password = request.form.get('password')
        code = request.form.get('code')

        key = 'VikiZ'

        totp = pyotp.TOTP(key)

        user = User.query.filter_by(email = email).first()

        if user:
            if check_password_hash( user.password, password ): #and totp.verify(code) == True:
                return redirect('http://localhost:8000/')
            

    return render_template("login.html")

@auth.route('/logout' )
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up' , methods = ["POST" , "GET"])

def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        new_user = User(email = email , first_name = username , password = generate_password_hash ( password , method = 'sha256' ) )
        db.session.add(new_user)
        db.session.commit()
        return redirect('http://localhost:8000/')
 
    return render_template("signup.html")


#leaderboard

'''data  = [
    ['Peter' , 'Software engineer' , '5000'],
    ['Amy' , 'Web Developer' , '3000'],
    ['Bob' , 'Scrum Master' , '10000'],
]

@auth.route('/leaderboard' , methods = ["POST" , "GET"])

def leaderboard():

    if request.method == 'GET':

        email = request.form.get('email')

        user = User.query.filter_by(email = email).first()

        #print(user.email)

    return render_template('leaderboard.html' , headings = headings , data = data)
'''


