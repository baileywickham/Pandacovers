from flask import Flask, flash, render_template, request, redirect, url_for
import flask_login
from flask_login import current_user

#this came from alex init, it may need to be changed with __init__.py. 
# Prepare flask and login manager for use
#TODO: autheticate user; check if user is auth and return index.html; also serve page to outside viewers

app = Flask(__name__)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def my_form():
        return render_template('login.html')



if __name__ == '__main__':
        app.run(debug=True)
