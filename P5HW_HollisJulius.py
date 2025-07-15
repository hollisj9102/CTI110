# Julius Hollis
# 7-15-2025
# P5HW - Game Project
# This program is a simple number guessing game.
# The user must guess a randomly selected number between 1 and 20.
# The game uses functions, loops, if/else, and the random library. 🎯

import random  # Importing random module to generate a random number

def create_player(name):
    # Returns a dictionary that holds the player's name and score
    return {
        'name': name,
        'score': 0
    }

def get_random_number():
    # This function returns a random number between 1 and 20
    return random.randint(1, 20)

def play_round(player):
    # This function allows the player to guess a number until they get it right
    number_to_guess = get_random_number()
    guess = 0
    tries = 0

    print("\n🎯 I'm thinking of a number between 1 and 20.")
    print("Try to guess it!")

    while guess != number_to_guess:
        guess = int(input("🔢 Enter your guess: "))
        tries += 1

        if guess < number_to_guess:
            print("Too low! 📉")
        elif guess > number_to_guess:
            print("Too high! 📈")
        else:
            print(f"🎉 Correct! You got it in {tries} tries.")
            player['score'] += 1  # Increase the player's score

def main():
    # Main function that starts the game
    print("🎮 Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")
    player = create_player(name)  # Create the player using a function

    rounds = 0
    for _ in range(10):  # Loop to play 10 rounds of the game
        play_round(player)
        rounds += 1

    print(f"\nGame Over, {player['name']}! 👋")
    print(f"You played {rounds} round(s) and guessed correctly {player['score']} time(s). 🏆")

# Start the game
main()
