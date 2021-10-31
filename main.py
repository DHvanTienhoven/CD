from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Home, sweet home.</p>'

@app.route('/greet/')
def greet():
    return '<h1>Hello, world!</h1>'

@app.route('/greet/<example_name>')
def greet_user(example_name):
    return f'<h1>Hello, {example_name}!</h1>'