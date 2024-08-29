from flask import Blueprint, render_template, request, redirect, url_for
from .game_logic import get_game_data, process_level

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # TODO: Initialize or reset game state if necessary
    data = get_game_data(level=1)
    return render_template('index.html', data=data)


# New route for grade selection
@main.route('/select-grade', methods=['GET', 'POST'])
def select_grade():
    if request.method == 'POST':
        selected_grade = int(request.form.get('grade'))
        # Logic to determine the recommended starting level based on grade
        if selected_grade in [7, 8]:
            starting_level = 1
        elif selected_grade in [9, 10]:
            starting_level = 2
        else:
            starting_level = 3  # Adjust as needed for higher grades

        return redirect(url_for('main.level', level=starting_level))

    return render_template('select_grade.html')

@main.route('/level/<int:level>', methods=['GET', 'POST'])
def level(level):
    if request.method == 'POST':
        player_input = request.form.get('player_input')
        success, feedback = process_level(level, player_input)

        if success:
            # Redirect to the next level
            next_level = level + 1
            return redirect(url_for('main.level', level=next_level))
        else:
            # Return the same level with feedback if the input was incorrect
            data = get_game_data(level=level)
            return render_template('level.html', data=data, feedback=feedback)

    data = get_game_data(level=level)
    return render_template('level.html', data=data)

# New route for roadmap navigation
@main.route('/roadmap')
def roadmap():
    total_levels = 5  # Set this to the total number of levels you have
    return render_template('roadmap.html', total_levels=total_levels)
