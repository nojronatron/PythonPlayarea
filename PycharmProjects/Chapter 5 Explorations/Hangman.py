# --------------------
# Author: Jon Rumsey
# Date: 5-May-2015
# Title: Hangman Game
# Description: A practical introduction to the List type
#   1. Computer picks a secret word and the player has to try to guess it one letter at a time
#   2. Each time the player makes an incorrect guess the computer shows a new image of a figure being hanged
#   3. If the player doesn't guess the word in time the stick figure is a 'goner'
# Version: Initial
# --------------------

# Lists are sequences (like Tuples) but ARE mutable
import random

# constants
HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
     |
     |
    ---------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
     |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |   -+-
     |
     |
     |
     |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |  /-+-
     |
     |
     |
     |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |  /-+-/
     |
     |
     |
     |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |
     |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   |
     |   |
     |
    ---------
    """,
    """
    ------
     |    |
     |    O
     |  /-+-/
     |    |
     |    |
     |   | |
     |   | |
     |
    ---------
    """
)

MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# initialize variables
word = random.choice(WORDS)  # the word to be guessed
so_far = "-" * len(word)  # one dash for each letter in word to be
wrong = 0  # number of wrong guesses player has made
used = []  # letters already guessed

# main loop
print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    # getting players guess
    guess = input("\n\nEnter your guess: ")
    guess = guess.upper()

    while guess in used:
        print("You've already guessed the letter", guess)
        guess - input("Enter your guess: ")
        guess - guess.upper()

    used.append(guess)

    # checking the guess
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        # create a new so-far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1

    # ending the game
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nYou've been hanged!")
    else:
        print("\nYou guessed it!")

print("\nThe word was", word)

input("\n\nPress the Enter key to exit.")