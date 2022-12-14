import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
""" A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
        """
class Die:


# 2) Create the class constructor. Use the following method comment.
    """     Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
    """
    def __init__(self):
        self.value = 0
        self.points = 0

# 3) Create the roll(self) method. Use the following method comment.
    """     Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
    """
    def roll(self):
        self.value = random.randint(1, 6) # Calls the random library imported at top, uses the 'randint()' function start value=1 end value=6. Will pick random numbers between and including 1 and 6.
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0
        print(f'This is the dice value - {self.value}, This is the roll points - {self.points}') # This line added by Matt for troubleshooting