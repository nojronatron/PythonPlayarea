__author__ = 'Orange'

# RandRange() produces a random integer.
# Simplest use is to use a single, positive, integer argument
# and it will return a random int from (and including) 0
# up to (but NOT including) that number.

import random

myRRNumber = random.randrange(6)

myRRNumber += 1
print(myRRNumber)

newNum = random.randrange(myRRNumber) + myRRNumber
print(newNum)

print("\nThe Rand Range function selected:", newNum)

input("\n\nPress the Enter key to exit. . .")