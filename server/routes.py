import os
from connect_4.game import Game, HumanAgent
from connect_4.ai.adversarial import AlphaBetaAgent
from connect_4.ai.q_learning import QLearningAgent
from server import app
from flask import render_template, jsonify, redirect, url_for, request, abort


@app.route('/')
def hello_world():
    return redirect(url_for('new_game_get'))


@app.route('/game/play')
def play_game():
    if game is None:
        return redirect(url_for('new_game_get'))
    return render_template('game.html')


@app.get('/game/new_game')
def new_game_get():
    return render_template('new_game.html')


@app.post('/game/new_game')
def new_game_post():
    global game
    if request.json['mode'] == 'single':
        mode = os.environ.get('AI_MODE', 'adversarial')
        if mode == 'adversarial':
            game = Game(AlphaBetaAgent(color=color2, min_color=color1), HumanAgent('Player1', color1))
        else:
            game = Game(QLearningAgent(color=color2), HumanAgent('Player1', color1))
    elif request.json['mode'] == 'multi':
        game = Game(HumanAgent('Player1', color1), HumanAgent('Player2', color2))
    else:
        abort(400)
    return redirect(url_for('play_game'))


@app.route('/api/drop_disc/<int:slot>')
def drop_disc(slot):
    if game is None:
        return 'Game has not been created!', 404
    disc = game.drop_disc(slot)
    winner = game.win()
    response = vars(disc)
    response['turn'] = game.turn
    response['winner'] = winner.__dict__() if winner else None
    return jsonify(response)


@app.route('/api/game_info')
def game_info():
    if game is None:
        return 'Game has not been created!', 404
    return jsonify(game.__dict__())


color1 = '#ffeb3b'
color2 = '#00bcd4'
game: Game | None = None
