# -------------------------------------------------#
# Title: Lab 6-1: Working with Functions
# Author: Jon Rumsey
# Date: 2-May-2015
# Desc: Create a function that prints the Sum, Difference, Product
#   and Quotient of to number
# ChangeLog: Initial
#-------------------------------------------------#

#-- Data --# 
# declare variables and constants

#-- Processing --#
def MathFunction(parmA, parmB):
    print("\nThe sum of", parmA, "and", parmB, "is: ", int(parmA) + int(parmB))
    print("The difference between", parmA, "and", parmB, "is: ", int(parmA) - int(parmB))
    print("The product of", parmA, "and", parmB, "is: ", int(parmA) * int(parmB))
    print("The quotient of", parmA, "and", parmB, "is: ", int(parmA) / int(parmB))

#-- Presentation (I/O) --#
firstNumber = input("\n\nEnter in a number: ")
secondNumber = input("\nEnter in another number: ")

MathFunction(firstNumber, secondNumber)

input("\nPress Enter key to quit.")
