# -------------------------------------------------#
# Title: Critter Caretaker Farm Program - Chpt 8 Challenge #4
# Author = Jonathan Rumsey
# Date: 12-July-2015 thru 19-July-2015
# Desc: Create a Critter_Caretaker program for a FARM of critters.
#       Instantiate several Critter objects and keep track of them through a list.
#       Mimic the Critter_Caretaker program but require the user take care of an entire farm of critters.
#       Each menu choice should allow the user to perform some action for all critters in the farm.
#       In addition, give each critter random starting hunger and boredom levels.
#  ChangeLog: Initial
# -------------------------------------------------#

import random


class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger, boredom):
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


def get_amount(of_what):
    """ Ask user how much food or how many minutes of playtime """
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


def all_critters_status(all_critters):
    for critter in all_critters:
        print(critter.name, "'s Hunger: ", critter.hunger, "; Mood: ", critter.mood, sep="")


def name_the_critter(which_one):
    print("What do you want to name your", which_one, end="")
    critter_name = (input(" critter? ").capitalize())
    return critter_name


def pick_a_number():
    return random.randrange(20)


def select_one_or_all_critters(all_critters_param):
    print("Which critter? ...or all critters? ")
    counter = 1
    for critter in all_critters_param:
        print(counter, "-", critter.name)
        counter += 1
    one_or_all_param = (input("Enter name of the critter or 'all' for all of them: ")).strip().capitalize()
    if one_or_all_param == "" or len(one_or_all_param) <= 0:
        print("Invalid entry. Returning to menu.")
    else:
        return one_or_all_param


def main():
    critter_1 = Critter(name_the_critter("first"), pick_a_number(), pick_a_number())
    critter_2 = Critter(name_the_critter("second"), pick_a_number(), pick_a_number())
    critter_3 = Critter(name_the_critter("third"), pick_a_number(), pick_a_number())
    critter_4 = Critter(name_the_critter("fourth"), pick_a_number(), pick_a_number())
    all_critters = [critter_1, critter_2, critter_3, critter_4]

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
            one_or_all = select_one_or_all_critters(all_critters)
            if one_or_all == "All":
                for critter in all_critters:
                    critter.talk()
            else:
                for critter in all_critters:
                    if critter.name == one_or_all:
                        critter.talk()
                        break

        # feed your critter
        elif choice == "2":
            amount = get_amount(choice)
            one_or_all = select_one_or_all_critters(all_critters)
            if one_or_all == "All":
                for critter in all_critters:
                    critter.eat(amount)
            else:
                for critter in all_critters:
                    if critter.name == one_or_all:
                        critter.eat(amount)
                        break

        # play with your critter
        elif choice == "3":
            amount = get_amount(choice)
            one_or_all = select_one_or_all_critters(all_critters)
            if one_or_all == "All":
                for critter in all_critters:
                    critter.play(amount)
            else:
                for critter in all_critters:
                    if critter.name == one_or_all:
                        critter.play(amount)
                        break

        # Test Area Option 5
        elif choice == "5":
            print("The total number of critters is: ", len(all_critters))
            all_critters_status(all_critters)
            input("Press the Enter key to continue...")

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the Enter key to exit.")
