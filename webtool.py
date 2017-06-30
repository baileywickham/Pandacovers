from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user
import MySQLdb

#TODO: login_user method, user_loader method
# Prepare flask and login manager for use

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'admin': 'password'}
app.secret_key = '1234' #TODO: THIS NEEDS TO BE CHANGED IN THE FUTURE

db = MySQLdb.connect(host="localhost",
		     user="root",
		     passwd="alexiscool",
		     db="panda-login")
cur = db.cursor() # Cursor is needed for executing queries

def user_exists(username):
	if cur.execute("SELECT * FROM Users WHERE username = '" + username + "'") != 0:
		return True
	return False
	# Non-zero value indicates that the user exists

def get_password(username):
	return cur.execute("SELECT password FROM Users WHERE username = '" + username + "'") #this is the line that is causing the problem.

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
	if not user_exists(username):
		flash('incorrect username or password') # Placeholder file, we need to sort out an error page
	password = get_password(username)
        user_id = 1234

        User = UserClass(username, user_id, active=True)
        if pw == password: # pw and password do not appear to be the same. Needs to be fixed
                login_user()
                return render_template('index.html')
	db.close()
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
