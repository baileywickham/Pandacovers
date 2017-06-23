from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("login.html")
@app.route('/', methods=['POST'])
def my_form_post():
    username = request.form['inputUsername']
    password = request.form['inputPassword']
if __name__ == '__main__':
    app.run()
