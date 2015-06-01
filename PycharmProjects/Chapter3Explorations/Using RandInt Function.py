__author__ = 'Orange'
# Craps Roller
# Demonstrates random number generation

import random

# Ggenerate random numbers 1 - 6
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

# make sure the integers are in ascending order
anotherDie = 0
firstDie = 0
secondDie = 0
totalWithBonusRoll = 0

if (die1 > die2):
    print("die1 (", die1, "), is larger than die2 (", die2, ")", sep='')
    firstDie = die2
    secondDie = die1

if (die2 > die1):
    print("die2 (", die2, "), is larger than die1 (", die1, ").", sep='')
    firstDie = die1
    secondDie = die2

if (die1 == die2):
    print("die1 (", die1, "), and die 2 (", die2, ") are equal. No third die roll.", sep='')
else:
    anotherDie = random.randint(firstDie, secondDie)
    print("The ", firstDie, " by ", secondDie, " sided die was rolled and it shows a ", anotherDie, "!", sep='')
    total += anotherDie
    print("Your total with this bonus roll added is: ", total, sep='')

input("\n\nPress the Enter key to exit. . .")
