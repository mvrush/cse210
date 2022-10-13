import random

class Hider:
    """The person hiding from the Seeker. 
    
    The responsibility of Hider is to keep track of its location and distance from the seeker. 
    
    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self):
        """Constructs a new Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self._location = random.randint(1, 1000) # Picks an original location for the hider using a random number.
        self._distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self): # This is a getter method to pull the data from the 'self._distance' list defined above.
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0: # We are using [-1] to check the value of the last item in the list. It was input by the 'watch_seeker()' method below.
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]: # We use [-1] and [-2] to compare from the end of the list. Compares the two values in the 'self._distance' list.
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]: # We use [-1] and [-2] to compare from the end of the list. Compares the two values in the 'self._distance' list.
            hint = "(>.<) Getting warmer!"
        return hint

    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0) # If the calculation from 'watch_seeker()' below equals 0 it's held in the last spot on the list [-1]. If this is true, the hider is found and it returns True.
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location()) # (NOT SURE WHY I NEED .get_location() here or how it accesses that function) Calculates the distance between the hider "self._location" and seeker "seeker.get_location()". abs() will get the Absolute Value of a number. i.e. turns a -5 into a 5.
        self._distance.append(distance) # appends the new value for 'distance' into the 'self._distance' list defined above.