# -------------------------------------------------#
# Title: Backward Messages
# Author = Jon Rumsey
# Date: 3-May-2015
# Desc: Create a program that gets a message from
#       the user and then prints it out backwards
# ChangeLog: initial
# --------------------------------------------------#

# -- Data --#
reversedInput = ""
position = 0

# -- Processing --#
# -- Presentation (I/O) --#
print("\tBackwards message program")
print("Enter in a word or phrase and this program will reverse it for you.")
userInput = input("Enter in your word or phrase: ")
tracker = userInput

while tracker:
    reversedInput += tracker[-1]
    position = len(tracker)
    tracker = tracker[:position - 1]

# print("reversedInput: ", reversedInput)
# print("Position: ", position)
# print("Tracker: ", tracker)

print("Reversed, that would be:")
print(reversedInput)

input("Press the Enter key to exit.")