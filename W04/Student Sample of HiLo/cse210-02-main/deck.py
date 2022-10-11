# Deck class for hilo game
from card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()

    def draw_card(self):
        # draws card and removes it from deck
        return self.cards.pop()

    def create_deck(self):
        # creates a 52 card deck
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        # randomizes deck
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()