__author__ = 'Blue'
# This program will flip a coin 100 times and return the number of Head and the number of Tails
import random

print("\nWelcome to the coin flip statistics program.")
print("This program will flip an imaginary coin 100 times,")
print("keeping track of the number of times the coin comes up")
print("heads, and the number of times it comes up tails.")
print("Statistics will be displayed at the end of 100 coin flips.\n")

# Set up a 100-cycle loop
count = 100
heads = 0
tails = 0
flipcoin = 0

# Within each loop pick a new random number, either 1 (Heads) or 2 (Tails)
while count > 0:
    flipcoin = random.randint(0, 1)
    if flipcoin:
        heads += 1
        count -= 1
        # print("Flipcoin Head: ", flipcoin)
        continue
    else:
        tails += 1
        count -= 1
        # print("Flipcoin Tail: ", flipcoin)
        continue

# Return to the user the number of each: Heads; Tails
print("\nAfter flipping the coin 100 times,")
print("the number of heads is", heads, "and")
print("the number of tails is ", tails, ".", sep="")

input("\n\nPress the Enter key to exit.")
