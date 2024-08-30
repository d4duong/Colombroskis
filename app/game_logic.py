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
            ),
            "question": "Download the file below and find the encypted password.",
            "file_link": "/static/files/level1_password.txt", 
            "final_answer": "J!gc@$fj3eq",
        },
        2: {
            "level": 2,
            "objective": "Decode the Encryption",
            "description": "You have found the encrypted password file. You need to decode it to access the base.",
            "hint": "Think about common encryption methods like ROT13 and substitution cipher. Try using an website like cyberChef to decode the message.",
            "question": "Decode the encrypted password and input the decrypted password into the answer bar."
        },
        3: {
            "level": 3,
            "objective": "Bypass the AI's Login Screen",
            "description": (
                "You have successfully infiltrated deeper into the AI's database. "
                "To infiltrate even further, you need to bypass the login screen set up by the AI. "
                "You do not know the login details, but luckily, the AI forgot to set up an anti-hacking program. "
                "This is because the arrogant AI thought humans do not know how to hack anymore since "
                "humans have relied on AI like ChatGPT for all their coding! However, being a hacker, "
                "you know that this login page is easily bypassable. Using the provided information below, "
                "bypass the login screen."
            ),
            "hint": (
                "Use SQL injection to bypass the login screen. Try entering the following into the username field:\n"
                "`' OR 1=1;--`\n"
                "Leave the password field blank or enter anything.\n"
                "This trick confuses the system into thinking you're a valid user."
            ),
            "question": "Bypass the login screen using the SQL injection technique described.",
            "final_answer": "' OR 1=1;--",
        },
    }
    return levels.get(level, {})

def process_level(level, player_input):
    # TODO: Implement the logic for checking the player's input against the correct answer]
    correct_answers = {
        1: "J!gc@$fj3eq",  # Final decrypted answer for Level 1
        2: "W!tp@$sw3rd",  # Answer for Level 2 (ROT13 decoding)
        3: "' OR 1=1;--",  # Answer for Level 3 (SQL injection)
        # TODO: Add more correct answers for additional levels
    }

    success = player_input == correct_answers.get(level)
    feedback = "Correct!" if success else "Try again. Remember the hint."
    return success, feedback
