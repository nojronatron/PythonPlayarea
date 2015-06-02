# -------------------------------------------------#
# Title: Practice with Dictionaries
# Author: Jon Rumsey
# Date:  2-May-2015
# Desc: Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed
# by keys, which can be any immutable type; strings and numbers can always be keys.
# Think of Dictionaries as an unordered set of key:value pairs
# ChangeLog: Original
#-------------------------------------------------#

#-- Data --# 
# declare variables and constants
lstRow1 = ["1", "Bob Smith", "BSmith@Hotmail.com"]
dictRow1 = {"ID": 1, "Name": "Bob Smith", "Email": "BSmith@Hotmail.com"}
dictRow2 = {"ID": 2, "Name": "Sue Jones", "Email": "SueJ@email.com"}
lstTable = [dictRow1, dictRow2]

#-- Processing --#
# perform tasks

#-- Presentation (I/O) --#
# get user input
# send program output

print("\nThe List:")
print(lstRow1)
print("The Dictionary (name:value pairs):")
print(dictRow1)

print("\nAn index (1) from the List:")
print(lstRow1[1])
print("An index (Name) from the Dictionary:")
print(dictRow1["Name"])

print("\nAdd a Dictionary to make a multi-dimensional list:")
print(dictRow2)
print("Place Dictionaries into a List:")
print(lstTable)

print("\nItems in the list 'Table':")
for row in lstTable:
    print(row)

print("\nDictionaries have extra functions and properties:")
print("--- items()")
for myKey, myValue in dictRow1.items():
    print(myKey, " = ", myValue)
print("--- values()")
print(dictRow1.values())
print("--- keys()")
print(dictRow1.keys())
