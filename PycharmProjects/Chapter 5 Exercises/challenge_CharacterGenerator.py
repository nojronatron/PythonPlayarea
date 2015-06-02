# -------------------------------------------------#
# Title: Character Generator
# Author = Jon Rumsey
# Date: 22-May-2015
# Desc: Player should be given a pool of 30 points to spend on four attributes
#        Strength, Health, Wisdom, and Dexterity
#        The player should be able to spend points from the pool on any attribute
#        and should also be able to take points from an attribute and put them
#        back into the pool.
# ChangeLog: Initial
# -------------------------------------------------#

# -- Data --# 
# declare variables and constants
intPlayerPoints = 40
INTFIGHTERSTRENGTH = 20
lstStrength = ["Strength", INTFIGHTERSTRENGTH]
INTFIGHTERHEALTH = 15
lstHealth = ["Health", INTFIGHTERHEALTH]
INTFIGHTERWISDOM = 10
lstWisdom = ["Wisdom", INTFIGHTERWISDOM]
INTFIGHTERDEXTERITY = 15
lstDexterity = ["Dexterity", INTFIGHTERDEXTERITY]
tplAttributes = (lstStrength, lstHealth, lstWisdom, lstDexterity)

# -- Processing --#
# perform tasks

# -- Presentation (I/O) --#
# get user input
# send program output

while True:
    print("Character Type: Fighter")
    print("Attributes:")
    # Print-out the character attributes for the user
    print(tplAttributes)
    print("\nRemaining Attribute Points: ", intPlayerPoints)
    print("\nWhat do you want to do?")
    print("Add - Add Points to an attribute")
    print("Return - Remove Points from an attribute, return to the pool")
    print("Quit - Done Changing Attributes")
    strUserCommand = (input("Type Add, Return, or Quit: ").lower().strip())
    if "quit" in strUserCommand:
        break

    # Add or Return selected
    strAttribToChange = (input("Pick an attribute:").lower().strip())
    strAttribToChange = strAttribToChange.capitalize()

    # Check to see that user entered something that can Add/Return points to/from
    if strAttribToChange in lstStrength[0] or lstHealth[0] or lstWisdom[0] or lstDexterity[0]:
        intAttribPoints = int(input("How many points?"))

        # Check for 0 (put user back at main menu)
        if intAttribPoints == 0:
            print("\nYou selected zero... returning to menu.")
            continue

        # Strength
        if strAttribToChange in lstStrength:
            # Don't allow user to 'steal' points from an attributes base value
            if strUserCommand == "return":
                if (lstStrength[1] - intAttribPoints) < INTFIGHTERSTRENGTH:
                    print("Return fewer points! Minimum strength points:", INTFIGHTERSTRENGTH)
                    continue
                else:
                    lstStrength[1] -= intAttribPoints
                    intPlayerPoints += intAttribPoints
                    print("Subtracted", intAttribPoints, "from", strAttribToChange, "returning them to the pool.\n")
                    continue

            # Don't allow user to 'steal' points from their allocation either
            elif strUserCommand == "add":
                if intAttribPoints > intPlayerPoints:
                    print("You don't have enough points to do this")
                    continue
                else:
                    lstStrength[1] += intAttribPoints
                    intPlayerPoints -= intAttribPoints
                    print("Added", intAttribPoints, "to", strAttribToChange, "\n")
                    continue
            else:
                print("Invalid command", strUserCommand, ". Please try again.")
                continue

        # Dexterity
        if strAttribToChange in lstDexterity:
            # Don't allow user to 'steal' points from an attributes base value
            if strUserCommand == "return":
                if (lstDexterity[1] - intAttribPoints) < INTFIGHTERDEXTERITY:
                    print("Return fewer points! Minimum strength points:", INTFIGHTERDEXTERITY)
                    continue
                else:
                    lstDexterity[1] -= intAttribPoints
                    intPlayerPoints += intAttribPoints
                    print("Subtracted", intAttribPoints, "from", strAttribToChange, "returning them to the pool.\n")
                    continue

            # Don't allow user to 'steal' points from their allocation either
            elif strUserCommand == "add":
                if intAttribPoints > intPlayerPoints:
                    print("You don't have enough points to do this")
                    continue
                else:
                    lstDexterity[1] += intAttribPoints
                    intPlayerPoints -= intAttribPoints
                    print("Added", intAttribPoints, "to", strAttribToChange, "\n")
                    continue
            else:
                print("Invalid command", strUserCommand, ". Please try again.")
                continue

        # Wisdom
        if strAttribToChange in lstWisdom:
            # Don't allow user to 'steal' points from an attributes base value
            if strUserCommand == "return":
                if (lstWisdom[1] - intAttribPoints) < INTFIGHTERWISDOM:
                    print("Return fewer points! Minimum strength points:", INTFIGHTERWISDOM)
                    continue
                else:
                    lstWisdom[1] -= intAttribPoints
                    intPlayerPoints += intAttribPoints
                    print("Subtracted", intAttribPoints, "from", strAttribToChange, "returning them to the pool.\n")
                    continue

            # Don't allow user to 'steal' points from their allocation either
            elif strUserCommand == "add":
                if intAttribPoints > intPlayerPoints:
                    print("You don't have enough points to do this")
                    continue
                else:
                    lstWisdom[1] += intAttribPoints
                    intPlayerPoints -= intAttribPoints
                    print("Added", intAttribPoints, "to", strAttribToChange, "\n")
                    continue
            else:
                print("Invalid command", strUserCommand, ". Please try again.")
                continue

        # Health
        if strAttribToChange in lstHealth:
            # Don't allow user to 'steal' points from an attributes base value
            if strUserCommand == "return":
                if (lstHealth[1] - intAttribPoints) < INTFIGHTERHEALTH:
                    print("Return fewer points! Minimum strength points:", INTFIGHTERHEALTH)
                    continue
                else:
                    lstHealth[1] -= intAttribPoints
                    intPlayerPoints += intAttribPoints
                    print("Subtracted", intAttribPoints, "from", strAttribToChange, "returning them to the pool.\n")
                    continue

            # Don't allow user to 'steal' points from their allocation either
            elif strUserCommand == "add":
                if intAttribPoints > intPlayerPoints:
                    print("You don't have enough points to do this")
                    continue
                else:
                    lstHealth[1] += intAttribPoints
                    intPlayerPoints -= intAttribPoints
                    print("Added", intAttribPoints, "to", strAttribToChange, "\n")
                    continue
            else:
                print("Invalid command", strUserCommand, ". Please try again.")
                continue

    else:
        print("\nPlease type a valid attribute.")
        continue

# break will take operational control down to here
print("\n\nHere are the final attributes of your character:")
print("Character Type: Fighter")
print("Attributes:")
# Print-out the character attributes for the user
print(tplAttributes)
print("\nRemaining Attribute Points: ", intPlayerPoints)
input("\nPress the Enter key to quit.")