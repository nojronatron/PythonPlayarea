# -------------------------------------------------#
# Title: The Simple Critter Program
# Author = Jonathan Rumsey
# Date: 3-July-2015
# Desc: First example of a class written in Python that:
#       Defines a critter using a Class
# ChangeLog: Initial
# -------------------------------------------------#

# Create a new class, based on an OBJECT
#   Class Names should begin with a capital letter (by convention)
#   By default, the first parameter of EVERY instance method MUST be 'self'


class Critter(object):
    """A virtual pet"""
    def talk(self):
        print("Hi. I'm an instance of class Critter.")

# -- Data --#
crit = Critter()

# -- Processing --#
# perform tasks

# -- Presentation (I/O) --#
crit.talk()

input("\n\nPress the Enter key to exit.")
