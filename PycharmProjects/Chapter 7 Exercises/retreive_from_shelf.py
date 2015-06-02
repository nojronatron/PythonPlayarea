# -------------------------------------------------#
# Title: Un-Pickle It
# Author = Jon Rumsey
# Date: 25-May-2015
# Desc: See 'shelveit.py'. This script demonstrates
#        retrieving shelved lists.
# ChangeLog: initial
# -------------------------------------------------#

import shelve

# open the shelved file for read-only
s = shelve.open("pickles2.dat", "r")

print("\nRetrieving lists from the shelved file:")

# gather and print the contained lists' results
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])

# close the file
s.close()

input("\n\nPress the Enter key to exit.")