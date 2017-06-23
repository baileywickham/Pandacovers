from flask import Flask
from flask import request
from flask import render_template
#this file was for testing flask with wsgi scripts, getting this to take data and store it from the page was the important parts.
app = Flask(__name__)
@app.route('/')
def my_form():
    return render_template("index.html")
@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['inputDate']
    target = open('tmp', 'w')
    target.write(text1)
if __name__ == '__main__':
    app.run()
