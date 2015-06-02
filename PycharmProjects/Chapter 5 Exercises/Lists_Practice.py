# -------------------------------------------------#
# Title: Practice using Lists
# Author: Jon Rumsey
# Date:  2-May-2015
# Desc: A built-in Python sequence. Despite its name it is more akin to an array in other languages
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
# declare variables and constants
lstRow1 = ["1", "Bob Smith", "BSmith@mail.com"]
tplRow1 = ("1", "Bob Smith", "BSmith@mail.com")

# Multi-dimensional meaning nested:
lstRow2 = ["2", "Sue Jones", "SueJ@mail.com"]
lstTable = [lstRow1, lstRow2]
lstRow3 = ["3", "Joe James", "JoeJames@mail.com"]

#-- Processing --#
# perform tasks
lstRow1.append("555-1234")
lstRow2.remove("SueJ@mail.com")

#-- Presentation (I/O) --#
# get user input
# send program output

print("A list:")
print(lstRow1)
print("\nA tuple:")
print(tplRow1)
print("\nMulti-dimensional list with appended phone and removed email:")
print(lstTable)
print("\nNow an Insert method will be used to insert a new row into spot zero:")
lstTable.insert(0, lstRow3)
print(lstTable)
print("\nAnd now, sorted:")
lstTable.sort()
print(lstTable)
