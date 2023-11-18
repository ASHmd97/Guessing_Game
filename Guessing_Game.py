import random

# Initialize variables to keep track of attempts
attempts_list = []
attempts = 0

# Welcome message
print("Hello!, Welcome to the guessing game")

# Get user's name and ask if they want to play
username = input("What's your name? ")
wanna_play = input(f"Hi, {username} Do you like to play the guessing game? (yes or no): ").lower()

# Function to display the current high score
def show_score():
    if not attempts_list:
        print("There's currently no high score, Start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")

# Check if the user wants to play
if wanna_play == "yes":
    show_score()
    rand_num = random.randint(1, 10)

elif wanna_play == "no":
    print("Nice, Thanks!")

# Main game loop
while wanna_play == "yes":
    try:
        # Get the user's guess
        guess_num = int(input("Pick a number between 1 and 10: "))
        
        # Validate the user's guess
        if guess_num < 1 or guess_num > 10:
            raise ValueError("Please guess a number within the given range")
        else:
            attempts += 1
        
        # Check if the guess is correct
        if guess_num == rand_num:
            print("Nice!, you got it :)")
            print(f"It took you {attempts} attempts")
            attempts_list.append(attempts)
            wanna_play = input(f"{username}, Do you want to play again? (yes or no): ").lower()
            
            # Reset variables for a new game
            if wanna_play == "yes":
                attempts = 0
                rand_num = random.randint(1, 10)
                show_score()
                continue
            elif wanna_play == "no":
                print("That's cool, have a good day!")

        # Provide hints for incorrect guesses
        elif guess_num < rand_num:
            print("It's lower")
        elif guess_num > rand_num:
            print("It's higher")

    # Handle input errors
    except ValueError as error:
        print(error)
