# -------------------------------------------------#
# Title: Critter Caretaker Farm Program - Chpt 8 Challenge #4
# Author = Jonathan Rumsey
# Date: 12-July-2015
# Desc: Create a Critter_Caretaker program for a FARM of critters.
#       Instantiate several Critter objects and keep track of them through a list.
#       Mimic the Critter_Caretaker program but require the user take care of an entire farm of critters.
#       Each menu choice should allow the user to perform some action for all critters in the farm.
#       In addition, give each critter random starting hunger and boredom levels.
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


def feed_one():
    """
    Feed just one critter. Ask user for critter name, then feed it.
    :return:
    """
    # TODO: complete function to get critter name, then send info
    return ""


def play_with_one():
    """
    Play with just one critter. Ask user for critter name, then play with it.
    :return:
    """
    # TODO: complete function to get critter name, then send info to appropriate object
    # not implemented function
    return ""


def create_farm():
    """
    Create a farm of critters. For now just 4. Maybe later do something more interesting
    :return:
    """
    # TODO: Think of other ways to generate and then display critters that is simple and portable
    print("\nCreating farm of critters...")
    critter1 = Critter(name="Critter1")
    critter2 = Critter(name="Critter2")
    critter3 = Critter(name="Critter3")
    critter4 = Critter(name="Critter4")
    farm_of_critters = [critter1, critter2, critter3, critter4]
    print("\nHere are the critters:")
    print(str(farm_of_critters))


def main():
    crit_name = input("What do you want to name your critter?: ")
    create_farm()

    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        # TODO: Rethink this menu to better re-use single-critter functions (why re-write single-critter functions?)
        print("""
            Critter Caretaker
            0 - Quit
            1 - Listen to your critters
            2 - Feed your critters
            3 - Play with your critters
            4 - Feed just one critter
            5 - Play with just one critter
            """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critters
        # TODO: Update to apply to all Critters in the farm
        elif choice == "1":
            crit.talk()

        # feed your critters
        # TODO: Update to apply to all critters in the farm
        elif choice == "2":
            amount = get_amount(choice)
            crit.eat(amount)

        # play with your critters
        # TODO: Update this to apply to all critters in the farm
        elif choice == "3":
            amount = get_amount(choice)
            crit.play(amount)

        # feed a single critter
        elif choice == "4":
            amount = get_amount(choice)
            crit.feed_one(amount)

        # play with a single critter
        elif choice == "5":
            amount = get_amount(choice)
            crit.play_with_one(amount)

        # hidden magic status menu item
        # TODO: Update this to apply to all critters in the farm
        elif choice == "6":
            print(crit.__str__())

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the Enter key to exit.")
