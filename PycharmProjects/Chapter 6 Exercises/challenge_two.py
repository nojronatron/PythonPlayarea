# -------------------------------------------------#
# Title: The Guess My Number Game pt.II
# Author = Jon Rumsey
# Date: 24-May-2015
# Desc: Based on the Guess My Number game from chapter 3.
#        Modify the project by reusing the function ask_number()
#        Bonus: Refactored into proper functions and docstrings
#        Challenge 3: Make a function called MAIN that runs the
#        code.
# ChangeLog: v.2.0 24-May-2015
# -------------------------------------------------#

# ----#
import random
the_number = random.randrange(1, 100, 1)
tries = 0
guess = 0


# -- Processing --#
def intro_game():
    """Introduce the game to the user."""
    print("\tWelcome to the Guess My Number Game pt.II !")
    print("\nGuess what number I am thinking of.")


def ask_number():
    """Ask user to guess a number, and return answer to process_guess."""
    return int(input("\nEnter a whole number between 1 and 100: "))


def process_guess(_guess):
    """Process the users guess."""
    global tries
    while _guess != the_number:
        _guess = ask_number()
        if _guess > the_number:
            print("\nWrong. Guess a little lower.")
        elif _guess < the_number:
            print("\nWrong. Guess a little higher.")
        tries += 1


def game_over():
    """End of game."""
    print("\n\nWell done! You guessed it! The number was", the_number, ".")
    print("\nIt took you", tries, "tries to correctly guess the number.")


def main():
    intro_game()
    process_guess(guess)
    game_over()
    input("\n\nPress the Enter key to exit.")

# -- Presentation (I/O) --#

main()