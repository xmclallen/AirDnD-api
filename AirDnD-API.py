# hello_world.py

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html', body='Hello World')

@app.route('/login')
def login():
    return render_template('base.html', body='Login is TBD')

@app.route('/listings')
def listings():
    return render_template('base.html', body='Listings are TBD')
