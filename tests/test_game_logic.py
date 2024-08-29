# TODO: Write unit tests for the game logic functions
def test_get_game_data():
    level_data = get_game_data(1)
    assert level_data["objective"] == "Breach the Perimeter Firewall"

def test_process_level():
    success, feedback = process_level(1, "/etc/firewall/config.txt")
    assert success
    assert feedback == "Correct!"
