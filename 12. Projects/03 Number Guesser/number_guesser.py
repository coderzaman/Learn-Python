import random
import os
import platform
os.environ['TERM'] = 'xterm-256color'

low = 1
high = 50


# Log For Testing Purpose
def app_log(message, log_file='app.log'):
    entry = f"{message}\n"
    with open(log_file, 'a') as file:
        file.write(entry)


# cler terminal
def clear_terminal():
    current_os = platform.system()

    if current_os == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Random Number Generator
def generate_random():
    return random.randint(low,high)


# User guess Validator
def take_input():
    validator = True
    user_guess = None
    while validator:
        try:
            user_guess = int(input("Enter the number within 1-50: "))
            if not high >= user_guess >= low:
                raise TypeError("Number Must be within 1-50.\n")
            return user_guess
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(f"Please Input Integer Value. {user_guess} is not a Integer Number.\n")


# Reset Option Validator
def reset_input_validator():
    reset = None
    validator = True
    while validator:
        try:
            reset = int(input("Want To Reset?\nPress 1: Reset\nPress 2: Exit\n\nPlease Enter Input: "))
            if reset == 1 or reset == 2:
                validator = False
                return reset
            else:
                raise TypeError("Invalid Selection\n")
        except TypeError as e:
                print(e)
        except ValueError as e:
            print(f"Please Input Integer Value. {reset} is not a Integer Number.\n")


# Reset Function
def reset_game():
    user_option = reset_input_validator()

    if user_option == 1:
        clear_terminal()
        start_game()
    else:
        clear_terminal()
        return


#Game Function
def start_game():
    random_number = generate_random()

    # Save randon_number to log for testing purpose
    app_log(random_number)

    for i in range(0,5):
        user_guess = take_input()

        if user_guess == random_number:
            clear_terminal()
            print("We Win!\n")
            break
        elif user_guess > random_number:
            print("Correct answer is smaller!\n")
        elif user_guess < random_number:
            print("Correct answer is greater!\n")
    else:
        clear_terminal()
        print("You lose!\n")

    reset_game()

# Game Start
start_game()