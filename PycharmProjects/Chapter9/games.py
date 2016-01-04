# -------------------
# Author: Jonathan Rumsey
# Title: Games Module
# Description: Demonstrates creating a Python Module
# Original: 30-July-2015
# Updated: <date>, <updater>
# -------------------


class Player(object):
    """ A player for a game. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep


def ask_yes_no(question):
    """ Ask a yes or no question.
    :param question: A string
    :return: String (y/n) response to the question
    """
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """ Ask for a number within a range.
    :param question: A string
    :param low: An integer
    :param high: An integer
    :return: An integer
    """
    response = None
    while response not in range(low, high + 1):
        response = int(input(question))
    return response

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the Enter key to exit.")