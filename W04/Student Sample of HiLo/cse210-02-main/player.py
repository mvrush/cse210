
from random import randint


class Player:

    def __init__(self, debug = False) -> None:
        self.name = None
        self.score = 300
        self.hand = []
        self.last_guess_low = False
        self.debug = debug
    
    def __str__(self):
        return f"{self.name} - {self.score}"

    def get_current_card(self):
        return self.hand[0]

    def get_guess(self) -> str:
        '''
        Gets input from user and returns H or L as a string.

        return value: 
        string -> H or L

        Debug mode: skips user input and alternates between responses H and L
        '''
        guess = None
        if self.debug:
            self.last_guess_low = not self.last_guess_low
            print(f"{self.name}, what is your guess?")
            return "H" if self.last_guess_low else "L"
        while not guess == "H" or not guess == "L":
            guess = str(input(f"{self.name}, make a guess (H or L): ")).upper()
            if guess == "H" or guess == "L":
                return guess
            elif guess == "Q":
                exit(0)
            print("Invalid entry, try again.")

    def get_name(self):
        '''
        Gets input for the player name and sets the self.name variable to it. 

        Debug mode: sets the self.name to Bot_Tony with a random int at the end.
        '''
        if self.debug:
            self.name = "Bot_Tony" + str(randint(0,100))
        
        while not self.name:
            try:
                self.name = str(input("Enter your name: "))
            except:
                pass


            


