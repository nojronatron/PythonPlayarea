# -------------------------------------------------#
# Title: Chapter 4: Word Jumble Game
# Author: Jon Rumsey
# Date:  3-May-2015
# Desc: Computer picks a random word from a list and jumbles it
#       User is asked to guess the word.
#       1. Create sequence of words
#       2. Pick one word randomly from the sequence
#       3. Create a new word sequence and re-arrange the letters to form the jumble
#       4. Loop the player through guesses
#       5. Congratulate player, ask if done/play again
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
jumble = ""

#-- Processing --#
word = random.choice(WORDS)
correct = word
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#-- Presentation (I/O) --#
print("\tWelcome to Word Jumble!")
print("\nUnscramble the letters to make a word.")
print("\n\nThe jumble is:", jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")

if guess == correct:
        print("\nThat's it! You guessed it!\n")

print("Thanks for playing.")
input("\n\nPress the Enter key to exit.")