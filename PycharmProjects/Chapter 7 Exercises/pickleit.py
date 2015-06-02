# -------------------------------------------------#
# Title: The Pickle It Program
# Author = Jon Rumsey
# Date: 24-May-2015
# Desc: Pickling means to preserve. In terms of data
#        the meaning is the same: Preserve data like
#        using vinegar to pickle veggies. Complex
#        pieces of data can be pickled, like a list
#        or a dictionary, and saved to a file. The
#        file type will be BINARY. Data will be
#        stored and served as LISTS.
# ChangeLog: initial
# -------------------------------------------------#

import pickle

# Create lists to Pickle
print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

# Open a new file, pickle the lists, close the file
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

input("\n\nPress the Enter key to exit.")