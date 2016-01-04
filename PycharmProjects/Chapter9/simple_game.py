# -------------------
# Author: Jonathan Rumsey
# Title: Simple Game
# Description: A simple game, demonstrating use of modules
# Original: 30-July-2015
# Updated: <date>, <updater>
# -------------------

import games
import random

print("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
    num = games.ask_number(question="How many players? (2 - 5): ", low=2, high=5)

    for i in range(num):
        name = input("Player name: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("\nHere are the game results:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nDo you want to play again? (y/n): ")

input("\n\nPress the Enter key to exit.")
