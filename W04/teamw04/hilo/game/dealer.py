import random

class Dealer:
    """  Deals a card for the player

    Args:
        self (Dealer): An instance of the dealer

    """
    def __init__(self):
        self.value = 0

    """  Generates a random card

        Args:
            self (Dealer): An instance of the dealer 
    """
    def draw(self): # This is a METHOD for pulling a random card held in the Dealer class.
        self.value = random.randint(1, 13)
    
""" These lines used to test the Dealer class

        print(f"this is your card - {self.value}")

dealer = Dealer()
dealer.draw()

"""