def get_game_data(level):
    # TODO: Define the game data for each level, including challenges, hints, and objectives
    levels = {
        1: {
            "objective": "Breach the Perimeter Firewall",
            "description": "You are a hacker trying to breach the AI's base. You need to find the entrance file with the encrypted password to enter the base.",
            "hint": "Use basic command-line navigation commands such as 'ls' (or 'dir' if on a Windows device) to list files and directories within a specific directory, 'cat <.txt file>' (or 'type <.txt file>' if on a windows device) to read the contents of a file and 'cd <directory>' to move to a specific dirctory.",
            "question": "Find the entrance.txt file and input the encrypted password into the answer bar.",
            "file_link": "/static/files/level1_password.txt",
            "final_answer": "W!tp@$sw3rd"
        },
        2: {
            "level": 2,
            "objective": "Decode the Encryption",
            "description": "You have found the encrypted password file. You need to decode it to access the base.",
            "hint": "Think about common encryption methods like ROT13 and substitution cipher. Try using an website like cyberChef to decode the message.",
            "question": "Decode the encrypted password and input the decrypted password into the answer bar."
        },
        # TODO: Add more levels with increasing complexity
    }
    return levels.get(level, {})

def process_level(level, player_input):
    # TODO: Implement the logic for checking the player's input against the correct answer]
    correct_answers = {
        1: "W!tp@$sw3rd",  # Final decrypted answer for Level 1
        2: "Hello World!",  # Example answer for Level 2 (ROT13 decoding)
        # TODO: Add more correct answers for additional levels
    }

    success = player_input == correct_answers.get(level)
    feedback = "Correct!" if success else "Try again. Remember the hint."
    return success, feedback
