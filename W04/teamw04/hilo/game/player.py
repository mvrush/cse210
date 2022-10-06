

""" Player is the person playing the game who has a score

    Player class is responsible for keeping track of the score

    Attributes:
        score (int): this will be the players total score

"""


class Player:
    """ Constructs a new instance of Player with a score attribute

    Args:
        self (Player): an instance of the player

    Methods:
        Add 100 points to score if guessed correctly
        Subtract 75 points if guessed incorrectly
    
    """

    def __init__(self):
        self.score = 0

    def add_points(self):
        self.score += 100

    def subtract_points(self):
        self.score -= 75


""" Following lines used to test Player class. Uncomment and run player.py to test this class"""
#player = Player()
#print(f"We start with {player.score} points")
#player.add_points()
#print(f"Then we add 100 points using 'add_points()' for a total of {player.score} points")
#player.subtract_points()
#print(f"Then we subtract 75 points using 'subtract_points() for a total of {player.score} points")