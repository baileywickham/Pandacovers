from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("login.html")
@app.route('/', methods=['POST'])
def my_form_post():
<<<<<<< HEAD
    username = request.form['inputUsername']
    password = request.form['inputPassword']
=======
    text1 = request.form['inputUsername']
    target = open('tmp', 'w')
    target.write(text1)
>>>>>>> 1a2daaca21b1109ecb4fd9a1c9bc15fb4bf49a0e
if __name__ == '__main__':
    app.run()
