from game.dealer import Dealer # Imports our Dealer class
from game.player import Player # Imports our Player class

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Dealer: Presents a card from 1-13.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card = [] # an empty array to add card values to
        self.is_playing = True # ATTRIBUTE Boolean
        self.hilo = ""
        self.player = Player() # assigns and instance or Player() class to the self.player variable

    def start_game(self):
        """ Starts the game by running the main game loop
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing: # Says do this loop while 'self.is.playing' is 'True'
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self): # This is a METHOD held in the Director class.
        """ Ask user if card is higher or lower
        
        Args:
            self (Director): an instance of Director.

        Methods: (these could maybe be moved to Player class)
            1. draw card and append to the 'card' list
            2. draw 2nd card and append to the 'card' list
            3. compare cards to see if 2nd is higher or lower than the 1st

        """
        dealer = Dealer() # Assigns an instance of the Dealer class to a variable called 'dealer'
        dealer.draw_card() # Draws a card using draw() function in the Dealer class
        self.card.append(dealer.value) # Appends value to 'self.card' in Director class
        print(f"\nThe card is: {self.card[0]}")
        self.hilo = input("Higher or lower? [h/l] ").lower() # Ask user for input choosing if next card will be higher or lower
        dealer.draw_card() # Calls the draw_card() function from the Dealer() class
        self.card.append(dealer.value)
        print(f"\nThe card was: {self.card[1]}")



    
    def do_updates(self):
        """ Add the total score

        Args:
            self (Director): an instance of Director.
        
        """
        print(f"You started out with {self.player.score} points")
        
        if self.hilo == "l" and self.card[1] < self.card[0]:
            self.player.add_points()
        
        elif self.hilo == "h" and self.card[0] < self.card[1]:
            self.player.add_points()
        
        elif self.card[0] == self.card[1]:
            self.player.score = self.player.score
            print(f"The cards were the same, no score change.")

        else:
            self.player.subtract_points()
    
    def do_outputs(self):
        #d1 = Director() # This line for troubleshooting
        #print(f"This is our card - {d1.card}") # This line for troubleshooting
        #print(f"This is our get_inputs card - {self.card}") # This line for troubleshooting
        print(f"Your score is now: {self.player.score}")                
        if  self.player.score > 0:
            keep_playing = input("\nPlay again? [y/n] ").lower()
            if keep_playing == 'n':
                print(f"\nThanks for playing!\n")
                self.is_playing = False # This sets 'self.is_playing' to False and breaks the While loop to end the game
        
        if self.player.score <= 0:
            self.is_playing = False # This sets 'self.is_playing' to False and breaks the While loop to end the game
            print(f"\nYou ran out of points, you lose. :(\n")

        else:
            self.card = [] # If player inputs 'y' and keeps playing, it empties the 'self.card' array in the Director class

