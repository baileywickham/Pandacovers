from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user

#this came from alex init, it may need to be changed with __init__.py. 
# Prepare flask and login manager for use
#TODO: autheticate user; check if user is auth and return index.html; also serve page to outside viewers

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'admin': 'password'}

@app.route('/')
def splash():
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
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
def index():
        return render_template('index.html')
@login_manager.user_loader
def user_loader(userid):
        pass


class UserClass(flask_login.UserMixin):
        def __init__(self, name, id, active=True):
                self.name = name
                self.id = id
                self.active = active
def is_active(self):
        return self.active
if __name__ == '__main__':
        app.run(debug=True)
