from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Home, sweet home.</p> '

@app.route('/greet')
def hello():
    return '<h1>Hello, world!</h1> '

@app.route('/greet/<name>')
def hello_2(name):
    return f"Hello, {escape(name)}!"

