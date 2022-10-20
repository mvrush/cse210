# This is our parachute class

class Parachute:
    """The displayed parachute. 
    
    The parachute will slowly disappear as the result of missed guesses of the word. 
    
    Attributes:
        _chute (list(str)) used to draw the parachute.
        -man (list(str)) used to draw the man

    """

    def __init__(self):
        """ Constructs a new parachute

        Args:
            self (parachute): An instance of parachute.
        """
        self._chute = ["  ___  ", " /___\ ", " \   / ", "  \ /  "] # The "_" before chute means it's private.
        self._man = ["   o   ", "  /|\  ", "  / \  ", "", "^^^^^^^"]
    
    def draw_chute(self):
        """METHOD will draw the chute
                
        Args:
            self (Parachute): An instance of Parachute.
        
        """
        for i in self._chute: # This loops through the list and prints the item in each index position.
            print(i)
    
    def draw_man(self):
        """METHOD will draw the man
                
        Args:
            self (Parachute): An instance of Parachute.
        
        """
        for i in self._man:
            print(i)

""" Following lines for testing purposes. Uncomment and run parachute.py to test. """
parachute = Parachute() # creates an instance of parachute using the 'Parachute()' class
parachute.draw_chute() # uses the 'draw_chute()' Method (function) to draw the parachute
parachute.draw_man() # uses the 'draw_man()' Method (function) to draw the man.
    
