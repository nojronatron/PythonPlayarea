# -------------------
# Author: Jonathan Rumsey
# Title: Challenge #2 - Create a one-card version of the game 'war'
# Description: Each player gets a single card and the player with the highest card wins. A work in progress.
# Original: 5-Jan-2016
# Updated: 6-Jan-2016; Attempting to get game mechanics working -jar
# -------------------


import games
import cards


class War_Card(cards.Card):
    """ A game of war card    """
    ACE_VALUE = 11

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
            if v > 11:
                v = 11
        else:
            v = None
        return v


class War_Deck(cards.Deck):
    """ A game of war deck of cards    """
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                self.cards.append(War_Card(rank, suit))

    def remaining(self):
        return len(self.cards)


class War_Hand(cards.Hand):
    """ A game of war hand of cards    """
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # If a card in the hand has a value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # Add up card values, treat each Ace as 11
        t = 0
        for card in self.cards:
            t += card.value

        # Determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == War_Card.ACE_VALUE:
                contains_ace = True

        # Just increment the value of the ace to 11
        if contains_ace:
            t += 10

        return t


class War_Player(War_Hand):
    """ A game of war player.    """
    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

    def tie(self):
        print(self.name, "tied")


class War_Game(object):
    """ A game of War    """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def __additional_cards(self, player):
        # Some trigger or gate might be needed here
        self.deck.deal([player])
        print(player, "gets a new card.")

    def play(self):
        # deal initial card to everyone
        self.deck.deal(self.players, per_hand=1)
        print("Here are the results of this round:")
        for player in self.players:
            print("Player:", player)
            print("Name:", player.name)
            print("Total:", player.total)
            print()

        # compare card values to determine the winner
        print("Sorted descending:", sorted(self.players, key=self.players.__str__, reverse=True) )
        ranked_list = []
        ranked_list = sorted(self.players, key=self.players.__str__, reverse=True)
        print("Ranked List:", ranked_list)
        self.players[0].win()


def main():
    print("\t\tWelcome to the Game of War!\n")

    names = []
    number = games.ask_number("How many players? (2 - 8): ", low=2, high=9)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()

    game = War_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nPress the Enter key to exit.")
