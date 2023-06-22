from server import app, game
from flask import render_template, jsonify


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/game')
def game_play():
    return render_template('game.html')


@app.route('/api/drop_disc/<int:slot>')
def drop_disc(slot):
    disc, win = game.drop_disc(slot)
    return jsonify(vars(disc))
