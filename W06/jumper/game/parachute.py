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
        for i in self._man: # This loops through the list and prints the item in each index position.
            print(i)
    
    
    def erase_chute(self, answer): # will receive 'answer' data from the Word class                
        if answer == True:
            for i in self._chute:
                print(i)
            for i in self._man:
                print(i)
        
        if answer == False:
            self._chute.pop(0) # Removes the item at index position 0. Note, if you don't specify an index position, pop() removes the last item on the list.
            for i in self._chute:
                print(i)
            for i in self._man:
                print(i)

        if len(self._chute) == 0:
            print(f"You're dead!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
            return # This 'return' statement takes effect only when this 'if' statement is reached and true. It ends the program.
    

    """ THIS IS THE FUNCTION I USED FOR TESTING """
    def erase_chute_test(self):
        valid_input = True
        while valid_input:
            answer = input("enter y or n: ")
            if answer == 'y' or answer == 'n':
                valid_input = True

                if answer == "y":
                    answer = True
                if answer == "n":
                    answer = False
                
                if answer == True:
                    for i in self._chute:
                        print(i)
                    for i in self._man:
                        print(i)
                
                if answer == False:
                    self._chute.pop(0) # Removes the item at index position 0. Note, if you don't specify an index position, pop() removes the last item on the list.
                    for i in self._chute:
                        print(i)
                    for i in self._man:
                        print(i)

                if len(self._chute) == 0:
                    print(f"You're dead!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
                    break # This 'break' statement takes effect only when this 'if' statement is reached and true. It ends the program.
                        
            else:
                print("Invalid input, please try again") # This else statement works with the input validation. When the answer is not 'y' or 'n' valid_input becomes false and this is printed and the loop runs again.




""" Following lines for testing purposes. Uncomment and run parachute.py to test. """
parachute = Parachute() # creates an instance of parachute using the 'Parachute()' class
parachute.draw_chute() # uses the 'draw_chute()' Method (function) to draw the parachute
parachute.draw_man() # uses the 'draw_man()' Method (function) to draw the man.
parachute.erase_chute_test()
    
