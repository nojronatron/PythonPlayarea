# -------------------------------------------------#
# Title: LAB 6-2: Working with Returned Lists
# Author: Jon Rumsey
# Date: 2-May-2015
# Desc: 1. Create a function that returns a list of the Sum,
#           Difference, Product, and Quotient of two numbers
#       2. Display the results to the user
#       3. Divide the program into data, processing, and
#           presentation sections
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
numberOne = 0
numberTwo = 0
numberReturned = 0

#-- Processing --#
def doMath(parmA, parmB):
    lstSum = int(parmA) + int(parmB)
    lstDiff = abs(int(parmA) - int(parmB))
    lstProd = int(parmA) * int(parmB)
    lstQuot = int(parmA) / int(parmB)
    lstReturn = [lstSum, lstDiff, lstProd, lstQuot]
    return lstReturn

#-- Presentation (I/O) --#
print("\tWelcome to the math functionatron!")
numberOne = int(input("\nEnter the first number: "))
numberTwo = int(input("Enter the second number: "))

lstData = doMath(numberOne, numberTwo)

print("\nResults are as follows... ")
print("The SUM of", numberOne, "and", numberTwo, "is", lstData[0])
print("The DIFFERENCE of", numberOne, "and", numberTwo, "is", lstData[1])
print("The PRODUCT of", numberOne, "and", numberTwo, "is", lstData[2])
print("The QUOTIENT of", numberOne, "and", numberTwo, "is", lstData[3])
print(lstData)

input("\nPress ENTER key to exit.")