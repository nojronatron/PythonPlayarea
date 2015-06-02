# -------------------------------------------------#
# Title: Chapter 6 Challenge Question 1
# Author = Jon Rumsey
# Date: 24-May-2015
# Desc: In the Tic-Tac-Toe game, improve the ask_number()
#        function so that it can be called with a step
#        value. Make the default value of one.
# ChangeLog: Initial
# -------------------------------------------------#

# -- Data --# 
# declare variables and constants


# -- Processing --#
def ask_number(question, low, high, step=1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


def human_move(board, human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARES, 1)
        if move not in legal:
            print("\nThat square is already occupied, foolish human. Choose another.\n")
    print("Fine...")
    return move

# -- Presentation (I/O) --#
# get user input
# send program output
