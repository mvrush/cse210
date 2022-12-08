# This is the scoring class programmed by -Matt Rushton-
# from game.casting.cast import Cast # Don't need this since we are catching the instance of 'class' from directory.py that was instantiated in __main__.py
from game.casting.cast import Cast

class Scoring(Cast):
    
    def __init__(self):
        #self._cast = Cast() # Don't need this anymore This creates an instance (instantiates) of our Cast() class giving us access to it's methods and public variables (I don't think the private ones)
        self._gold_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._gold_score'. It holds our cumulative score
        self._silver_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._gold_score'. It holds our cumulative score
        self._coal_score = 0 # This adds another Attribute found only in our Scoring() class called 'self._gold_score'. It holds our cumulative score

    """ #old way of doing it that was looping the scoring
    def set_score(self, cast): # recieves the 'cast' instance from the call in 'director.py' which is actually an instance of our 'Cast()' class instantiaed in __main__.py
        #self._total_score += 100 # This line for testing only

        artifacts = cast.get_actors("artifacts") #  __main__.py runs first and uses an instance of the 'Cast()' class called 'class' That's where it's populated. This passes the 'artifacts' key to 'get_actors()' in the 'cast' insance of 'Cast()' class
        # print(artifacts) # prints the list of the object values of 'artifacts' in the cast which it pulls from the 'director.py' from an instance of 'Cast()' found in __main__.py. Uses the 'get_text()' function from the 'Actor()' class.
        for artifact in artifacts:
            #print(artifact.get_text()) # I think I am calling the 'get_text()' function from the Actor() class to pull the text out of the artifact object.
                # To fix this next part I think I need to create an array or something with all the * and 0 values. Somehow I need to check only a single artifact in one position and it seems
                # to be looping through all of them continuously.
            if artifact.get_text() == "*":
                print("It was an astrisk")
                self._total_score += 1
            elif artifact.get_text() == "0":
                print("It was a zero")
                self._total_score -= 1
        
        return self._total_score
    """
    # New way of doing it where it just passes the 'text' value of the matched artifact
    def set_score(self, text, score):
        if text == "G":
            print("It was a 'G'")
            self._gold_score = self._gold_score + score
            return self._gold_score
        elif text == "S":
            print("It was an 'S'")
            self._silver_score = self._silver_score + score
            return self._silver_score
        elif text == "C":
            print("It was a 'C'")
            self._coal_score = self._coal_score + score
            return self._coal_score
    
    def get_score(self, mineral):

        if mineral == "gold":
            return self._gold_score
        elif mineral == "silver":
            return self._silver_score
        elif mineral == "coal":
            return self._coal_score

    def clear_score(self):
        self._gold_score = 0
        self._silver_score = 0
        self._coal_score = 0    

