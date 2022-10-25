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

        self._is_playing = True # ATTRIBUTE sets the boolean 'True' to show we are currently playing
        self._parachute = Parachute() # ATTRIBUTE calls the Parachute() class and creates an instance of it called self._hider.
        self._word = Word() # ATTRIBUTE calls the Word() class and creates an instance of it called self._word.
        self._terminal_service = TerminalService() # ATTRIBUTE calls the TerminalService() class and creates an instance of TerminalService() and assigns it to self._terminal_service
        self._guess = True # ATTRIBUTE this is a class variable for the guesses, default is set to True until overwritten by a function.
        self._no_chute = None # ATTRIBUTE Set this to none to match return values from Parachute() 'erase_chute()' when there is still a chute.
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

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
        # print(self._no_chute) # Used this line to test whether or not I was getting a boolean or None value returned from 'erase_chute()' in Parachute() class.
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
            if word_complete == False:
                self._get_inputs()
        # if word_complete becomes True it goes 'to _do_outputs()'.            



    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if self._no_chute == True:
            self._terminal_service.write_text(f"Ya'll died foo. Your parachute is gone. See that 'x' for a head? That mean you dead.\n") # prints this out using the 'write_text()' function from 'TerminalService()'
            play_again = "" # defines the variable 'play_again' so I can do input validation using a 'while' loop.
            while play_again not in ("y", "n"): # If they input anything other than 'y' or 'n' it keeps asking. 'not in' means 'does not include'
                play_again = input("Play again? [y or n]: ").lower() # takes user input, changes it to lower case using the 'lower()' function and stores it in the 'play_again' variable.
            if play_again == "y":
                self._word = Word() # ATTRIBUTE calls the Word() class and creates an instance of it called self._word. Did this to reset the random word
                self._parachute = Parachute() # ATTRIBUTE calls the Parachute() class and creates an instance of it called self._parachute. Did this to reset the parachute
                self._guess = True # ATTRIBUTE this is a class variable for the guesses, sets it back to "True" until overwritten by a function.
                self._is_playing = True
            
            #elif play_again == "n":
            else:
                self._terminal_service.write_text(f"\nThanks for playing Jumper!")
                print() # Prints a blank line to make it look nicer when the program ends.
                self._is_playing = False # Changes 'self._is_playing' to False to end the game loop.
        
        else:
            word = self._word.print_clue() # This actually runs the 'print_clue()' function and prints it as the final completed word. It recieves the return (which is the completed word) from 'print_clue()' and stores it in the 'word' variable.
            self._parachute.erase_chute(self._guess) # Passes the boolean True or False from 'self._guess' to the 'erase_chute()' function in the Parachute() class. Prints the chute one last time at whatever state it was in.
            self._terminal_service.write_text(f"You did it! The word was: {''.join(word)}\n") # Here we use the 'join()' function to iterate through the string values in the list and join them toghther. If I wanted a space between each item I could put a space between the ''
            # print("".join(word)) # Uncomment this to see how the 'join()' function works on ths list.
            play_again = "" # defines the variable 'play_again' so I can do input validation using a 'while' loop.
            while play_again not in ("y", "n"): # If they input anything other than 'y' or 'n' it keeps asking. 'not in' means 'does not include'
                play_again = input("Play again? [y or n]: ").lower() # takes user input, changes it to lower case using the 'lower()' function and stores it in the 'play_again' variable.
            if play_again == "y":
                self._word = Word() # ATTRIBUTE calls the Word() class and creates an instance of it called self._word. Did this to reset the random word
                self._parachute = Parachute() # ATTRIBUTE calls the Parachute() class and creates an instance of it called self._parachute. Did this to reset the parachute
                self._is_playing = True
            
            #elif play_again == "n":
            else:
                self._terminal_service.write_text(f"\nThanks for playing Jumper!")
                print() # Prints a blank line to make it look nicer when the program ends.
                self._is_playing = False # Changes 'self._is_playing' to False to end the game loop.
            


""" NEXT LINES FOR TESTING ONLY """
#director = Director() # Creates in instance of the director class I can use to test functions.
#director.start_game() # Runs the 'start_game()' function