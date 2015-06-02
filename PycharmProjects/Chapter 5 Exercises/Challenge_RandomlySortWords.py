# -------------------------------------------------#
# Title: Random List Resorter
# Author = Jon Rumsey
# Date: 22-May-2015
# Desc: Create a program that prints a list of words in random order
#    The program should print all the words and not repeat any.
# ChangeLog: Initial
# -------------------------------------------------#

# -- Data --# 
# declare variables and constants
import random
lstWords = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot"]
lstNewOrder = []

# -- Processing --#
# perform tasks


def rearrangeList(lstOriginal):
    strPickedWord = ""
    while True:
        strPickedWord = random.choice(lstWords)
        lstNewOrder.append(strPickedWord)
        lstWords.remove(strPickedWord)
        if len(lstWords) <= 0:
            return lstNewOrder
        continue

# -- Presentation (I/O) --#
# get user input
# send program output
print("The original list of words is:\n", lstWords)

lstNewListOrder = rearrangeList(lstWords)
print("\nThe new list of words is now:\n", lstNewListOrder)

input("\nPress Enter to quit.")