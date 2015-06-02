# -------------------------------------------------#
# Title: Computer Counter
# Author: Jon Rumsey
# Date: 3-May-2015
# Desc: Write a program that counts for the user.
#       Let the user enter the starting number,
#       the ending number, and the amount by
#       which to count.
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
startNum = 0
stopNum = 0
increment = 1

#-- Processing --#
# perform tasks

#-- Presentation (I/O) --#
print("\tComputer Counting Program")
print("\nEnter a beginning and ending number,")
print("and the amount to count by. The computer")
print("will count through the numbers by that amount.")

while("True"):
    startNum = int(input("\nEnter the starting number: "))
    stopNum = int(input("Enter the ending number: "))
    increment = int(input("Enter the amount by which to count: "))

    for i in range(startNum, stopNum + 1, increment):
        print(i)

    if "y" == (input("\nDone! Again (y/n)?").lower().strip()):
        continue
    else:
        break

input("\n\nWell, okay then...Press the Enter key to exit.")