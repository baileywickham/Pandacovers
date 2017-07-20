from flask import Flask, flash, render_template, request, redirect, url_for, make_response, session
import flask_login
from flask_login import current_user
import pymysql
from functools import wraps
pymysql.install_as_MySQLdb()

#TODO: login_user method, user_loader method
# Prepare flask and login manager for use

"""
if sha256_crypt.verify(password, dbpass):
              session['username'] = data['username']
"""

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.secret_key = '1234'
db = pymysql.connect(host="74.91.125.179",
		     user="bailey-vs",
		     passwd="alexiscool",
		     db="panda-login")
'''
db =pymysql.connect(host="localhost",
  		     user="root",
   		     passwd="alexiscool",
  		     db="panda-login")
'''
@app.route('/')
def main():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    return redirect(url_for('splash'))

def requireLogged(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			return redirect(url_for('home'))
	return wrap

def user_exists(username):
	cur = db.cursor()
	if cur.execute("SELECT * FROM Users WHERE username = '{0}'".format(username)):
		cur.close()
		return True
	cur.close()
	return False
	# Non-zero value indicates that the user exists

def get_password(username):
    cur = db.cursor()
    result = cur.execute("SELECT * FROM Users WHERE username = '{0}'".format(username))
    if result > 0:
        data = cur.fetchone()
        user_pass = data[4]
    else:
        flash('incorect username')
    cur.close()
    return user_pass
	# After gathering password, sha256 should be verified, see random paste above

def get_id(username):
	cur = db.cursor()
	result = cur.execute("SELECT * FROM Users WHERE username = '{0}'".format(username))
	if result > 0:
		data = cur.fetchone()
		user_id = data[5] # This location could be wrong, I did it from memory
	cur.close()
	return user_id

@app.route('/login')
def splash():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['inputUsername']
        pw = request.form['inputPassword']
    app.logger.info(pw)
    if not user_exists(username):
        flash('incorrect username')
        return render_template('login.html')
    user_id = get_id(username)
    dbpassword = get_password(username)
    User = UserClass(username, user_id, active=True) # Do we actually need this? I think the same effect can be done with cookies
    if pw == dbpassword:
        session['logged_in'] = True
#        session['isManager'] = bool(Manager) I am going to consolidate managers and users into one table with a 1 or 0 value for manager
        session['username'] = username
        return redirect(url_for('home')) 
    else:
        flash('incorrect password')
        return render_template('login.html')

def logout(user):
	flask_login.logout_user()
	flash('Logged out successfully')

@login_manager.unauthorized_handler
def unauthorized():
	return 'Unauthorized: you need to be logged in.'

@app.route('/home')
#@requireLogged
def home():
	return render_template('index.html')
"""
@app.route('/home', methods=['GET', 'POST']
def smscall():
	if request.method == 'POST'
		when = form.request('inputDate')
		where = form.request('inputLocation') #use where[:4] to grab the first 4 digits to call the store by number.
		postition = form.requset('inputFob')
		textingLocations = form.request('inputAskingLocations')
		additonaltext = form.request('extraText')
"""		
@login_manager.user_loader
def user_loader(userid):
    pass
# This is where the user object will be created using UserClass, this will likely be called from login_user# This is where the user's session gets initiated

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
