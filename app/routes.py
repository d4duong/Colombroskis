from flask import Blueprint, render_template, request, redirect, url_for, make_response
from .game_logic import get_game_data, process_level

main = Blueprint('main', __name__)

@main.route('/clear_all_cookies')
def clear_all_cookies():
    # Create a response object
    response = make_response(redirect(url_for('main.index')))
    
    # Iterate through all cookies and set them to expire in the past
    for cookie in request.cookies:
        response.set_cookie(cookie, '', expires=0)
    
    return response

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_grade = int(request.form.get('grade'))
        
        # Logic to determine the recommended starting level based on grade
        if selected_grade in [7, 8]:
            starting_level = 1
        elif selected_grade in [9, 10]:
            starting_level = 2
        else:
            starting_level = 3  # Adjust as needed for higher grades

        # Redirect to the starting level based on selected grade
        return redirect(url_for('main.level', level=starting_level))

    # Render the grade selection form
    return render_template('index.html')

@main.route('/select-language', methods=['POST'])
def select_language():
    lang = request.form.get('language')
    response = make_response(redirect(request.referrer))
    response.set_cookie('lang', lang)
    return response

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


