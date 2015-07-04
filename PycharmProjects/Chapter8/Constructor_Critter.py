# -------------------------------------------------#
# Title: Constructor Critter program
# Author = Jon Rumsey
# Date: 3-July-2015
# Desc: Demonstrate a simple Constructor to create multiple objects.
# ChangeLog: Initial
# -------------------------------------------------#


class Critter(object):
    """A virtual pet"""
    def __init__(self):
        print("A new critter has been born!")
        # This is the Constructor (Initialization) Method

    def talk(self):
        print("\nHi. I'm an instance of class Critter.")

# -- Data --# 
# declare variables and constants

# -- Processing --#
# perform tasks

# -- Presentation (I/O) --#
# main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nPress the Enter key to exit.")
