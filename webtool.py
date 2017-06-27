from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user

#TODO: add database, login_user method, user_loader method, return userid and pw from database
# Prepare flask and login manager for use

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'admin': 'password'}

#return loginpage on first login
@app.route('/')
def splash():
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
        #fake userid because database doesnt exist yet. replace username == admin with a database check,
        #including checking passwords
        if request.method == 'POST' and 'inputUsername' in request.form:
                username = request.form['inputUsername']
                pw = request.form['inputPassword']
        user_id = 1234
        User = UserClass(username, user_id, active=True)
        if username == 'admin' and pw == 'password':
                login_user()
                return render_template('index.html')
        else:
                print ('incorrect password')
        return render_template('login.html')

def login_user():
        pass 
#lol

@login_manager.user_loader
def user_loader(userid):
        pass

#this creates a user object, the usermixin is a premade flask user_login class.
#this will probably need to be rewritten at somepoint
class UserClass(flask_login.UserMixin):
        def __init__(self, name, id, active=True):
                self.name = name
                self.id = id
                self.active = active
def is_active(self):
        return self.active
#remove debuger for production
if __name__ == '__main__':
        app.run(debug=True)
