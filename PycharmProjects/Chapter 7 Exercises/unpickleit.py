# -------------------------------------------------#
# Title: Un-Pickle It
# Author = Jon Rumsey
# Date: 25-May-2015
# Desc: See 'pickleit.py'. This file will load the
#        'pickled' (bin) file data into lists and
#        print them out.
# ChangeLog: initial
# -------------------------------------------------#

import pickle

# read data from the file and unpickle it
print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

# print the unPickled lists
print(variety)
print(shape)
print(brand)

# close the file
f.close()

input("\n\nPress the Enter key to exit.")