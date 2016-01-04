# -------------------------------------------------#
# Title: Critter Caretaker Program
# Author = Jonathan Rumsey
# Date: 3-July-2015
# Desc: Charge the user with the care of his/her own virtual pet. Learning objectives:
#       Create classes to define objects; Write methods and create attributes for objects;
#       Instantiate objects from classes; Restrict access to an object's attributes.
# ChangeLog: Initial
#            11-July-2015 Began working on Chp8 Challenges
# -------------------------------------------------#


class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        # print("Hunger:", self.hunger, "; Boredom:", self.boredom)
        self.__pass_time()

    def eat(self, food):
        print("Brruppp. Thank you for the", food, "units of food!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Wheee!!! Thank you for the", fun, "minutes of playtime!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def getamount(ofwhat):
    """ Ask user how much food or how many minutes of playtime """
    if ofwhat == "2":
        howmuch = int(input("Feed your critter how many servings?"))
        if howmuch <= 0:
            print("That is too little food.")
            howmuch = 0
        elif howmuch >= 11:
            print("That is too much food!")
            howmuch = 10
    elif ofwhat == "3":
        howmuch = int(input("Play with your critter for how many minutes?"))
        if howmuch <= 0:
            print("That is not enough playtime.")
            howmuch = 0
        elif howmuch >= 11:
            print("That is too much playtime!")
            howmuch = 10
    return howmuch


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print("""
            Critter Caretaker

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            amount = getamount(choice)
            crit.eat(amount)

        # play with your critter
        elif choice == "3":
            amount = getamount(choice)
            crit.play(amount)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the Enter key to exit.")
