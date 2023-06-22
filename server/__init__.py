from flask import Flask
from connect_4.game import Game
from connect_4.player import HumanAgent


app = Flask(__name__)
game = Game(HumanAgent('p1', 'red'), HumanAgent('p2', 'blue'))
from . import routes
