# -------------------
# Author: Jonathan Rumsey
# Title: Pickle Practice
# Description: Practice working with Pickle, which will store and recover PYTHON objects in a filesystem
# Original: 1-Dec-2015
# Updated: <date>, <updater>
# -------------------

import sys
import pickle


def read_pickle_contents_aloud(filename):
    print("Reading contents of Pickle file:")
    with open(filename, 'rb') as rb:
        contents = pickle.load(rb)
        print(contents)


def write_pickle_file(stuff_to_write, filename):
    print("Writing stuff to Pickle file", filename.__str__())
    with open(filename, 'wb') as wb:
        pickle.dump(stuff_to_write, wb, pickle.HIGHEST_PROTOCOL)


print("The filename will be:", end="")
my_file = "./my_data_file.pickle"
print(my_file.__str__())

print("\nCreating a pickle file with some dictionary values:")
my_dictionary = {
    "administrator": "P@55W0rd!",
    "power user": "P@55W0rd@",
    "standard user": "password",
    "guest": "guest"
}
print("Username\t\tPassword")
print("========\t\t========")
for item in my_dictionary:
    print(item, "\t\t", my_dictionary[item], sep="")

print("\nUse PICKLE to dump the dictionary to a file.")
write_pickle_file(my_dictionary, my_file)

print("\nHere is the result:")
read_pickle_contents_aloud(my_file)

print("\n\n")
input("Press the Enter key to exit.")
