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
            if len(self._chute) != 0: # This says, it the length of 'self._chute' does not (!) equal zero, loop through 'self._man' and print each index content.
                for i in self._man:
                    print(i)

        if len(self._chute) == 0:
            self._man[0] = "   x   " # if the length gets to zero, changes the content of index position [0] in 'self._man' to an 'x' to replace the head of our man.
            for i in self._man:
                print(i)
            end_game = print(f"You fell!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
            return end_game # This 'return' statement takes effect only when this 'if' statement is reached and true. It ends the program.
    

    """ THIS IS THE FUNCTION I USED FOR TESTING """
    def erase_chute_test(self):
        for i in self._chute: # This loops through the list and prints the item in each index position to print chute.
            print(i)   

        for i in self._man: # This loops through the list and prints the item in each index position to print man.
            print(i)
        
        valid_input = True
        # As long as 'valid_input' remains true, the loop runs. It only turns to false if user inputs anything other than 'y' or 'n' OR
        # The loop runs until the last 'if' statement becomes true and is sets 'valid_input' to False
        while valid_input:
            answer = input("Wanna live jumper? Enter y or n: ")
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
                    if len(self._chute) != 0: # This says, it the length of 'self._chute' does not (!) equal zero, loop through 'self._man' and print each index content.
                        for i in self._man:
                            print(i)

                if len(self._chute) == 0:
                    self._man[0] = "   x   " # if the length gets to zero, changes the content of index position [0] in 'self._man' to an 'x' to replace the head of our man.
                    for i in self._man:
                        print(i)
                    print(f"You're dead!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
                    valid_input = False # This changes 'valid_input' to False to end the loop.
                    #break # This 'break' statement takes effect only when this 'if' statement is reached and true. It ends the program. It's another way to end the loop
                        
            else:
                print("Invalid input, please try again") # This else statement works with the input validation. When the answer is not 'y' or 'n' valid_input becomes false and this is printed and the loop runs again.




""" Following lines for testing purposes. Uncomment and run parachute.py to test. """
parachute = Parachute() # creates an instance of parachute using the 'Parachute()' class
#parachute.draw_chute() # uses the 'draw_chute()' Method (function) to draw the parachute
#parachute.draw_man() # uses the 'draw_man()' Method (function) to draw the man.
parachute.erase_chute_test()
    
