# -------------------------------------------------#
# Title: Chapter 5 Review - Lab 5-1: Working with Lists
# Author: Jon Rumsey
# Date:  2-May-2015
# Desc: 1. Create an application that uses a list to hold data
#       2. Add code that lets user append a new row of data
#       3. Add a loop that lets user keep adding rows
#       4. As user if they want to save data to a file when they exit the loop
#       5. Save the data to a file if response is 'yes'
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
lstRow1 = [1, "Bob Smith", "BSmith@Hotmail.com"]
lstRow2 = [2, "Sue Jones", "SueJ@Yahoo.com"]
lstRow3 = [3, "Joe James", "JoeJames@Gmail.com"]
lstTable = [lstRow1, lstRow2, lstRow3]

#-- Processing --#
# perform tasks

#-- Presentation (I/O) --#
print("\nDictionary of List (row) items:")
for row in lstTable:
    print(row)

while True:
    if "y" == (input("\nDo you want to add to this list (y/n)? ").lower().strip()):
        intID = len(lstTable) + 1
        strName = (input("\nEnter user name: ").title().strip())
        strEmail = (input("\nEnter user's Email address: ").lower().strip())
        newRow = [intID, strName, strEmail]
        lstTable.append(newRow)
        continue
    else:
        break

print("\nTest output to show added row to existing lstTable:")
for row in lstTable:
    print(row)

if "y" == (input("\nDo you want to save this list to a file (y/n)? ").lower().strip()):
    objFile = open(".\Lab5-1_data.txt", "w")
    for row in lstTable:
        objFile.write((str(row)) + "\n")
    objFile.close()
    print("\nFile 'Lab5-1_data.txt' was written to the current directory.")

input("Press Enter key to quit.")