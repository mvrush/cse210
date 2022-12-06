#merged from RFK
import pyray
from game.shared.point import Point


class KeyboardService:

    #Merged from RFK
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    
    
    #Originally in Batter
    """A keyboard service inteface."""

    def is_key_down(self, key):
        """Detects if the given key is being pressed.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is being pressed; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_pressed(self, key):
        """Detects if the given key was pressed once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was pressed once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_released(self, key):
        """Detects if the given key was released once.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key was released once; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")
    
    def is_key_up(self, key):
        """Detects if the given key is released.
        
        Args:
            key: A string containing the key value, e.g. 'a', '0', etc.

        Returns:
            True if the key is released; false if otherwise.
        """
        raise NotImplementedError("not implemented in base class")