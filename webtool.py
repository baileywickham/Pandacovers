from flask import Flask, flash, render_template, request, redirect, url_for, g
import flask_login
from flask_login import current_user
import MySQLdb
import plivo
from functools import wraps


#TODO: login_user method, user_loader method
# Prepare flask and login manager for use

"""
if sha256_crypt.verify(password, dbpass):
              session['username'] = data['username']
"""

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'admin': 'password'}
app.secret_key = '1234' #TODO: THIS NEEDS TO BE CHANGED IN THE FUTURE

auth_id = ''
auth_token = ''
#p = plivo.RestAPI(auth_id, auth_token)

#params = { 'src' : 'xxxxxxxxx', dst : '123456789<123456789', text : 'hello from bailey'} 
#response = p.send_message(params)
#move this to a call function on post method.

db = MySQLdb.connect(host="localhost",
		     user="root",
		     passwd="alexiscool",
		     db="panda-login")
#CURSORS MUST BE INSIDE METHODS OR ELSE IT CRASHES, NO GLOBAL CURSORS. cur = db.cursor()
@app.route('/')
def splash():
	if User.is_autenticated:
		return redirect(url_for('home'))
	else:
		return redirect(url_for('login'))
		
def user_exists(username):
	cur = db.cursor()
	if cur.execute("SELECT * FROM Users WHERE username = %s", [username]) != 0:
		return True
	return False
	# Non-zero value indicates that the user exists

def get_password(username):
	cur = db.cursor()
	result = cur.execute("SELECT * FROM Users WHERE username = '" + username + "'")
	if result > 0:
		data = cur.fetchone()
		dbpass = data[4]
	return dbpass
	# After gathering password, sha256 should be verified, see random paste above

@app.route('/login')
def loginfunc():
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
                username = request.form['inputUsername']
                pw = request.form['inputPassword']
		app.logger.info(pw)
	if not user_exists(username):
		flash('incorrect username')

	password = get_password(username)
	user_id = 1234
       	User = UserClass(username, user_id, active=True)
        if pw == password:
                login_user()
                return redirect(url_for('home')) 
	else:
		flash('incorrect password')
        return render_template('login.html')

def login_user():
        pass 
#lol

@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/home', methods=['GET', 'POST'])
def smscall():
	if request.method == 'POST':
		when = form.request('inputDate')
		where = form.request('inputLocation') #use where[:4] to grab the first 4 digits to call the store by number.
		postition = form.requset('inputFob')
		textingLocations = form.request('inputAskingLocations')
		additonaltext = form.request('extraText')
	
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
def login_required(g):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			return redirect(url_for('login', next=request.url))
		return f(*args, **kwargs)
	return decorated_function


#remove debuger for production
if __name__ == '__main__':
        app.run(debug=True)
