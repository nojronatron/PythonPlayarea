# -------------------------------------------------#
# Title: Critter Caretaker Program - Chpt 8 Challenge #3
# Author = Jonathan Rumsey
# Date: 12-July-2015
# Desc: Building off of the Critter_Caretaker program,
#       add a 'hidden' menu option to view critter's
#       status using the ___str__(self) built-in method.
#  ChangeLog: Initial
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

    def __str__(self):
        magic_response = "Critter object\n"
        magic_response += "name: " + self.name + "\n"
        magic_response += "hunger: " + str(self.hunger) + "\n"
        magic_response += "boredom: " + str(self.boredom) + "."
        return magic_response

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


def get_amount(of_what):
    """ Ask user how much food or how many minutes of playtime """
    how_much = 0
    if of_what == "2":
        how_much = int(input("Feed your critter how many servings?"))
        if how_much <= 0:
            print("That is too little food.")
            how_much = 0
        elif how_much >= 11:
            print("That is too much food!")
            how_much = 10
    elif of_what == "3":
        how_much = int(input("Play with your critter for how many minutes?"))
        if how_much <= 0:
            print("That is not enough playtime.")
            how_much = 0
        elif how_much >= 11:
            print("That is too much playtime!")
            how_much = 10
    return how_much


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
            amount = get_amount(choice)
            crit.eat(amount)

        # play with your critter
        elif choice == "3":
            amount = get_amount(choice)
            crit.play(amount)

        # hidden magic status menu item
        elif choice == "4":
            print(crit.__str__())

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the Enter key to exit.")
