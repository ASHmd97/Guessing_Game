import random

def welcome_message():
    """Displays the welcome message for the guessing game."""
    print("Hello! Welcome to the guessing game")

def get_username():
    """Gets the user's name as input."""
    return input("What's your name? ")

def ask_to_play(username):
    """Asks the user if they want to play the guessing game."""
    return input(f"Hi, {username}! Do you want to play the guessing game? (yes or no): ").lower()

def show_score(attempts_list):
    """Displays the current high score."""
    if not attempts_list:
        print("There's currently no high score. Start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

def play_game(username):
    """Manages the main game loop."""
    attempts_list = []
    
    while True:
        show_score(attempts_list)
        rand_num = random.randint(1, 10)
        attempts = 0

        while True:
            try:
                guess_num = int(input("Pick a number between 1 and 10: "))

                if guess_num < 1 or guess_num > 10:
                    raise ValueError("Please guess a number within the given range")

                attempts += 1

                if guess_num == rand_num:
                    print("Nice! You got it :)")
                    print(f"It took you {attempts} attempts")
                    attempts_list.append(attempts)
                    break

                elif guess_num < rand_num:
                    print("It's higher")

                elif guess_num > rand_num:
                    print("It's lower")

            except ValueError as error:
                print(error)

        play_again = input(f"{username}, do you want to play again? (yes or no): ").lower()

        if play_again != "yes":
            print("That's cool, have a good day!")
            break

if __name__ == "__main__":
    # Start the game
    welcome_message()
    username = get_username()
    wanna_play = ask_to_play(username)

    if wanna_play == "yes":
        play_game(username)
    else:
        print("Nice, thanks!")
