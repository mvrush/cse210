from game.dealer import Dealer

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Dealer: Presents a card from 1-13.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = 0
        self.is_playing = True # ATTRIBUTE Boolean

    def start_game(self):
        """ Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        self.do_updates()
        self.do_outputs()

    def do_updates(self):
        dealer = Dealer()
        dealer.draw_card() # Draws a card using draw() function in the Dealer class
        self.card = dealer.value #possibly updates 'self.card' in Director class?
        #print(f"This is our do_updates card - {self.card}")
    
    def do_outputs(self):
        d1 = Director()
        print(f"This is our card - {d1.card}")
        print(f"This is our do_updates card - {self.card}")
