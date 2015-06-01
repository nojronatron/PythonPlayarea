__author__ = 'Blue'
# This program simulates a future cookie.
import random

print("\tWelcome to the Fortune Cookie Simulator!")
print("\nThis program will display your fortune.")

# Generate a random number between 0 and 4
picker = random.randint(1, 4)

# Depending on what number was selected, one of five 'fortunes' should be displayed
# each time the program is run

print("\nYour fortune is as follows...")

if picker <= 1:
    print("Good luck is in your future!")
elif picker == 2:
    print("You will have a tough day ahead.")
elif picker == 3:
    print("Someone you know will call you soon.")
else:
    print("Clouds are gathering. Hunker down and plan for the future!")

input("\n\nPress the Enter key to exit...")