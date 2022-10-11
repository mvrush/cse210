# Card class for hilo game
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def show(self):
        print("{} of {}".format(self.value, self.suit))
