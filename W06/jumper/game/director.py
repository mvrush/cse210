from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.word import Word

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachute (Parachute): The parachute that disappears as a result of missed guesses.
        is_playing (boolean): Whether or not to keep playing.
        word (Word): The hidden word which the user is trying to guess.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self._parachute = Parachute() # ATTRIBUTE calls the Parachute() class and creates an instance of it called self._hider.
        self._is_playing = True # ATTRIBUTE sets the boolean 'True' to show we are currently playing
        self._word = Word() # ATTRIBUTE calls the Word() class and creates an instance of it called self._word.
        self._terminal_service = TerminalService() # ATTRIBUTE calls the TerminalService() class and creates an instance of TerminalService() and assigns it to self._terminal_service
        self._guess = True # ATTRIBUTE this is a class variable for the guesses, default is set to True until overwritten by a function.
        self._no_chute = None # ATTRIBUTE Set this to none to match return values from Parachute() 'erase_chute()' when there is still a chute.
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        #self._parachute.draw_chute() # Draws the initial parachute
        #self._parachute.draw_man() # Draws the initial man
        while self._is_playing: # says, while 'self_is_playing' is True, keep running this loop.
            self._get_inputs() # 'get_inputs()' method. Gets user input from TerminalService()
            self._do_updates() # 'do_updates()' method. Advances the game one step
            self._do_outputs() # 'do_outputs()' method. Sends output to TerminalService() do display to user

    def _get_inputs(self): # This is a private (_) METHOD held in the Director class
        """Gets input from the user.

        Args:
            self (Director): An instance of Director.
        """
        self._word.print_clue()
        self._no_chute = self._parachute.erase_chute(self._guess) # Passes the boolean True or False from 'self._guess' to the 'erase_chute()' function in the Parachute() class. Receives the returned boolean from 'self._parachute.erase_chute()' and stores it in the 'no_chute' variable
        print(self._no_chute)
        if self._no_chute == None:
            letter_guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ") # 'read_letter()' can have prompts to ask user for letter input.
            self._guess = self._word.check_guess_matches(letter_guess) # calls the 'guessed_letter()' function from the Word() class held in 'self._word' instance. Passes the guessed letter from user input in the previous line to that function then stores the returned True or False in the 'self._guess' value defined in class variables
        return self._no_chute # Returns the value for 'self._no_chute'

    def _do_updates(self):
        """Keeps watch on if the word is guessed an updates the parachute.

        Args:
            self (Director): An instance of Director.
        """
        #self._word.check_guess_matches(self._parachute.erase_chute()) # This will call the 'correct_guess()' function from the Word() class and give it access to the Parachute() class by passing  'self._parachute' so that it can send the True or False value to the Parachute() class
        #print(self._word.check_guess_matches())
        #guess_boolean = self._word.check_guess_matches()        
        word_complete = self._word.word_match_complete()
        #self._parachute.erase_chute(self._guess) # Passes the boolean True or False to the 'erase_chute()' function in the Parachute() class.
        while word_complete == False and self._no_chute == None:
            word_complete = self._word.word_match_complete() # We run this again to check and see if the word_complete is now true.
            self._get_inputs()
        # if word_complete becomes True it goes 'to _do_outputs()'.            



    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        parachute = self._parachute.erase_chute() # Calls the 'draw_chute()' function from the Parachute() class
        self._terminal_service.write_text(parachute) # Uses the TerminalService() class and passes the variable value 'parachute' to the 'write_text()' Method function to draw the parachute


""" NEXT LINES FOR TESTING ONLY """
#director = Director() # Creates in instance of the director class I can use to test functions.
#director.start_game() # Runs the 'start_game()' function