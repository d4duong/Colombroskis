def get_game_data(level):
    # TODO: Define the game data for each level, including challenges, hints, and objectives
    levels = {
        1: {
            "level": 1,
            "objective": "Breach the Perimeter Firewall",
            "description": "You are a hacker trying to breach the AI's base. You need to find the entrance file with the encrypted password to enter the base.",
            "hint": (
                "Download the file and navigate to the Downloads directory using the following commands:\n"
                "1. `cd Downloads`\n"
                "2. `ls` (to list the files in the directory)\n"
                "3. `cat level1_password.txt` (to view the content of the file)\n"
                "Then, use CyberChef to decrypt the password using ROT13."
            ),
            "question": "Download the file below and find the encypted password.",
            "file_link": "/static/files/level1_password.txt", 
            "final_answer": "W!tp@$sw3rd",
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
