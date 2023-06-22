from server import app
from flask import render_template


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/game')
def game():
    return render_template('game.html')
