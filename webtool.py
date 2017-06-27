from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user

#this came from alex init, it may need to be changed with __init__.py. 
# Prepare flask and login manager for use
#TODO: autheticate user; check if user is auth and return index.html; also serve page to outside viewers

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
app.secret_key = 'thisissupersecret'

@app.route('/welcome', methods=['GET', 'POST'])
def my_form():
	return render_template("login.html")

users = {'user': {'pw': 'password'}} # Temporary dictionary, mysql will be later implemented
class User(flask_login.UserMixin):
	pass

@app.route('/create', methods=['GET', 'POST'])
def create_post():
	date = request.form['inputDate']
	location = request.form['inputLocation']
	fob = request.form['inputFoB']
	askLocation = request.form['inputAskingLocation']
	extraText = request.form['extraText']

@login_manager.user_loader
def user_loader(username, methods=['GET', 'POST']): # Prepares user for non-login activities
	if username not in users:
		return
	user = User()
	user.id = username
	flash('this is the user_loader method')
	return user

@login_manager.request_loader
def request_loader(request, methods=['GET', 'POST']):
	username = request.form.get('inputUsername')
	if username not in users:
		return
	user = User()
	user.id = username
	flash('this is the request loader method')
	user.isauthenticated = request.form['inputPassword'] == users[username]['inputPassword']
	return user

@app.route('/templates/login', methods=['GET', 'POST'])
def login():
	flash('login method')
	if flask.request.method == 'GET':
		return
	username = flask.request.form['inputUsername']
	if flask.request.method == 'POST':
		if flask.request.form['inputPassword'] != users[username]['inputUsername']:
			flash('incorrect credentials')
		else:
			user = User()
			user.id = email
			flask_login.login_user(user)
			return redirect(url_for('create'))
	return render_template('login.html')
if __name__ == "__main__":
    app.run()
