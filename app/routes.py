from flask import Blueprint, render_template, request
from .game_logic import get_game_data, process_level

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # TODO: Initialize or reset game state if necessary
    data = get_game_data(level=1)
    return render_template('index.html', data=data)

@main.route('/level/<int:level>', methods=['GET', 'POST'])
def level(level):
    if request.method == 'POST':
        # TODO: Process player input and move to the next level or provide feedback
        player_input = request.form.get('player_input')
        success, feedback = process_level(level, player_input)

        if success:
            # TODO: Redirect to the next level or display victory screen if it's the final level
            return render_template('level_complete.html', level=level)
        else:
            # TODO: Return the same level with feedback if the input was incorrect
            data = get_game_data(level=level)
            return render_template('level.html', data=data, feedback=feedback)

    data = get_game_data(level=level)
    return render_template('level.html', data=data)
