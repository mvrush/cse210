from game.terminal_service import TerminalService
from game.hider import Hider
from game.seeker import Seeker


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._hider = Hider() # ATTRIBUTE calls the Hider() class as a function. Creates an instance of Hider() and assigns it to self._hider
        self._is_playing = True # ATTRIBUTE sets the boolean 'True' to show we are currently playing
        self._seeker = Seeker() # ATTRIBUTE calls the Seeker() class as a function. Creates an instance of Seeker() ans assigns it to self._seeker
        self._terminal_service = TerminalService() # ATTRIBUTE calls the TerminalService() class as a function. Creates an instance of TerminalService() and assigns it to self._terminal_service
        
    def start_game(self): # This is a METHOD held in the Director class
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing: # says, while 'self._is_playing' is True, keep running this 3-step loop.
            self._get_inputs() # 'get_inputs()' method. Detects user input
            self._do_updates() # 'do_updates()' method. Advances the game one step
            self._do_outputs() # 'do_outputs()' method. Shows the the user what happened

    def _get_inputs(self): # This is a METHOD held in the Director class
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        new_location = self._terminal_service.read_number("\nEnter a location [1-1000]: ") # Calls the 'read_number()' function in the TerminalService() class held in the 'self.terminal_service' attribute defined above. Passes the string prompting user for input.
        self._seeker.move_location(new_location) # Calls the 'move_location()' function from the Seeker() class held in the 'self._seeker' attribute above. Passes the user's input for the 'new_location' variable on the line just above this one.
        
    def _do_updates(self): # This is a METHOD held in the Director class
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # This next line is very tricky for me to try and understand. -Matt
        self._hider.watch_seeker(self._seeker) # Calls the 'watch_seeker()' function from the Hider() class held in the 'self._hider' attribute defined above. Passes the Seeker() class held in the 'self._seeker' attribute there so it can access the self._location held there.
        
    def _do_outputs(self): # This is a METHOD held in the Director class
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._hider.get_hint() # Calls the 'get_hint()' function from the Hider() class held in the 'self._hider' attribute above. Holds it in the 'hint' variable here.
        self._terminal_service.write_text(hint) # Uses the TerminalService() class and passes the variable value 'hint' to the 'write_text()' Method function
        if self._hider.is_found(): # calls the 'is_found()' function in the Hider() class held in the 'self._hider' attribute defined above
            self._is_playing = False # sets the '_is_playing' attribute to False to end the game.