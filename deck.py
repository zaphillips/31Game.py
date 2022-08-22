from card import Card
import random

class Deck():
    def __init__(self):
        self.deck = []
        self.suites = ["H", "C", "S", "D"]
        self.names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q', 'A']
        for suit in self.suites:
            for name in self.names:
                cards = Card(suit, name)
                value = cards.returnValue()
                self.deck.append(suit + " " + name + " " + str(value))

    def shuffle(self):
        random.shuffle(self.deck)

    def show(self):
        for cards in range(len(self.deck)):
            print(self.deck[cards])

    def draw(self):
        return self.deck.pop(0)

    def count(self)-> int:
        return len(self.deck)