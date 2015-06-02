# -------------------------------------------------#
# Title: Un-Pickle It
# Author = Jon Rumsey
# Date: 25-May-2015
# Desc: See 'pickleit.py' and unpickleit.py. This
#        script will demonstrate shelving lists
#        together in a single file. The shelve
#        module create a random-access dictionary
#        for accessing the lists.
# ChangeLog: initial
# -------------------------------------------------#

import shelve

# Create a shelf
print("\nShelving lists.")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
# a shelf key can only be a string

# flush the buffer to the file
s. sync()

# close the file
s.close()

input("\n\nPress the Enter key to exit.")