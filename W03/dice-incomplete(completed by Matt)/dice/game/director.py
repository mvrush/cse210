from game.die import Die


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dice = [] # ATTRIBUTE Creates an empty list to add the dice to.
        self.is_playing = True # ATTRIBUTE Boolean, is the Director playing (Director in this case is invoked by the player)
        self.score = 0 # ATTRIBUTE The score for each roll
        self.total_score = 0 # ATTRIBUTE The total score for all rolls

        for i in range(5): # Here we use a 'for' loop to create 5 instances of the 'die' using the 'Die()' function.
            die = Die() # We create each 'die' using the 'Die()' class imported from our 'die.py' using 'import Die' at the top.
            self.dice.append(die) # Each time through the loop we append a die to the 'dice' array defined in the attributes of Director above. 

    def start_game(self): # This is a METHOD held in the Director class
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs() # 'get_inputs()' method. Detects user input
            self.do_updates() # 'do_updates()' method. Advances the game one step (basically rolls dice, adds the score)
            self.do_outputs() # 'do_outputs()' method. Shows the the user what they rolled and their score

    def get_inputs(self): # This is a METHOD held in the Director class
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """ 
        roll_dice = input("Roll dice? [y/n] ") # Asks the user for a boolean input 'y' or 'n' and stores it in the 'roll_dice' variable
        self.is_playing = (roll_dice == "y") # if the 'roll_dice' variable is equal to (==) 'y' it stores the boolean 'True' in the 'self.is_playing' attribute
        # After the above two steps are complete it returns to the 'start_game(self)' method then does the 'do_updates' metho
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing: # This 'if' block says 'if 'self.is_playing' is NOT True, then return to Director and it ends the program
            return 

        for i in range(len(self.dice)): # Loops through the 'self.dice' list and rolls each dice
            die = self.dice[i] # pulls out each dice in the list
            die.roll() # rolls the dice using the 'roll()' function defined in the Die class
            self.score += die.points  # Adds the individual score of that die to the 'self.score' attribute in Director
        self.total_score += self.score # Adds the current 'self.score' to the 'self.total_score' attributes in Director

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)): # Loops through the 'self.dice' list.
            die = self.dice[i] # Creates a new list from the 'self.dice' list and assigs it to the 'die' variable
            values += f"{die.value} " # Adds each 'die.value' to a 'values' variable as a string element. You end up with a string of values.

        print(f"You rolled: {values}") # Displays the 'value' variable which is the string of values created in the above 'for' loop.
        print(f"Your score is: {self.total_score}\n") # Displays the value of 'self.total_score' held in that attribute of Director
        self.is_playing == (self.score > 0) # If the score is greater than '0' that means we picked 'Y' to roll again. So this sets 'self.is_playing' attribute to boolean 'True' so it runs again.