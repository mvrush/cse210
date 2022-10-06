import random

""" A dealer who deals cards.

    Dealer class responsibility is to draw a random card to present to the player

    Attributes:
        value (int): This will be the value of the card.

"""


class Dealer:
    """  Constructs a new instance of Dealer with a card value attribute

    Args:
        self (Dealer): An instance of the dealer
    
    Methods:
        Will generate a random card with values 1 to 13

    """
    def __init__(self):
        self.value = 0

    def draw_card(self): # This is a METHOD for pulling a random card held in the Dealer class.
        self.value = random.randint(1, 13)
    


        """ Following lines used to test the Dealer class. Uncomment and run dealer.py to test this class. """

        #print(f"this is your card - {self.value}")

#dealer = Dealer() # creates an instance of dealer using the 'Dealer()' class
#dealer.draw_card() # uses the 'draw_card()' Method (function) to draw a random card

