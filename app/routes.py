from flask import Blueprint, render_template
from .game_logic import get_game_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    data = get_game_data()
    return render_template('index.html', data=data)
