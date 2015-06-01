__author__ = 'Orange'
import random

# In pseudo code first

# Welcome the player to the game and explain it
print("\tWelcome to the Guess My Number Game!")
print("\nGuess what number I am thinking of.")

# The computer must pick a random number between 1 and 100
the_number = random.randrange(1, 100, 1)

# set the number of player guesses to 1
tries = 1
guess = 0

# while the player's guess does not equal the random number:
while guess != the_number:

    guess = int(input("\nEnter a whole number between 1 and 100: "))

    # if the guess is greater than the number
    if guess > the_number:
        # tell the player to guess lower
        print("\nWrong. Guess a little lower.")

    # otherwise
    elif guess < the_number:
        # tell the player to guess higher
        print("\nWrong. Guess a little higher.")

    # get a new guess from the player

    # increase the number of guesses by 1
    tries += 1

# congratulate the player on guessing the number
print("\n\nWell done! You guessed it! The number was", the_number, ".")

# let the player know how many guesses it took
print("\nIt took you", tries, "tries to correctly guess the number.")

input("\n\nPress the Enter key to exit.")
