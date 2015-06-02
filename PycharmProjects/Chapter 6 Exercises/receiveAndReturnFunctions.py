# -------------------------------------------------#
# Title: Receive and Return
# Author = Jon Rumsey
# Date: 23-May-2015
# Desc: <description of script>
# ChangeLog: Initial
# -------------------------------------------------#

# -- Data --# 
# declare variables and constants

# -- Processing --#
def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower().strip()
    return response

# -- Main --#
display("Here's a message for you.\n")

number = give_me_five()
print("here's what I got from give_me_five():", number)

answer = ask_yes_no("\nPlease enter 'y' or 'n': ")
print("Thanks for entering:", answer)

input("\n\nPress the Enter key to exit.")
