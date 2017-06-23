from flask import Flask
import flask_login

# Prepare flask and login manager for use
app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

users = {'user': {'pw': 'password'}} # Temporary dictionary, mysql will be later implemented
class User(flask_login.UserMixin):
	pass

@login_manager.user_loader
def user_loader(username): # Prepares user for non-login activities
	if username not in users:
		return
	user = User()
	user.id = username
	return user

@login_manager.request_loader
def request_loader(request):
	username = request.form.get('inputUsername')
	if username not in users:
		return
	user = User()
	user.id = username

	user.isauthenticated = request.form['inputPassword'] == users[username]['inputPassword']
	return user

@app.route('/templates/login', methods=['GET', 'POST'])
def login():
	if flask.request.method == 'GET':
		return
	username = flask.request.form['inputUsername']
	if flask.request.form['inputPassword'] == users[username]['inputUsername']:
		user = User()
		user.id = email
		flask_login.login_user(user)
		return flask.redirect(flask.url_for('protected'))
	return 'alert.("badlogin")'

if __name__ == "__main__":
    app.run()
