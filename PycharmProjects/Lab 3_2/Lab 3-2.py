__author__ = 'Orange'
import sys

# Get the argument value
# Execute if 1, 2, or 3 is selected
# Print "You choose one" only if option 1 is selected.
# Print "You choose two" only if option 2 is selected.
# Print "You choose three" only if option 3 is selected.
# Print "Please choose 1, 2, or 3"

if (len(sys.argv) > 1):
    # Could have saved sys.argv[1] as an int(sys.argv[1]) to use as an int in each of the following lines of code
    if (sys.argv[1] == "1"):
        print("You choose one.")
    if (sys.argv[1] == "2"):
        print("You choose two.")
    if (sys.argv[1] == "3"):
        print("You choose three.")
    else:
        print("Please enter a single choice: 1, 2, or 3.")
else:
    print("Please choose 1, 2, or 3.")

input("Press Enter to exit. . .")