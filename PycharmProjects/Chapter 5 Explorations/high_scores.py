# Author: Jon Rumsey
# Title: High Scores program
# Description: List methods do the work to manipulate a List type
# Original: May 2015
# Updated: 8-May-2015

scores = []
choice = None

while choice != "0":
    print(
        """
        High Scores

        0 - Exit
        1 - Show Scores
        2 - Add a Score
        3 - Delete a Score (disabled)
        4 - Sort Scores (deprecated)
        """
    )
    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")

    # list high score table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)

    # add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("What was your score?"))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)   # Sort in hi/low order
        scores = scores[:5]  # Keep only the top 5 scores

    # remove a score
#    elif choice == "3":
#        score = int(input("Remove which score? "))
#        if score in scores:
#            scores.remove(score)
#        else:
#            print(score, "isn't in the high scores list.")

    # sort the scores
#    elif choice == "4":
#        scores.sort(reverse=True)

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the Enter key to exit.")
