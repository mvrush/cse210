#merged from RFK
import pyray

class VideoService:
    #merged from RFK
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        #image = actor.get_image() # This line just pulls the address to the image and then it holds the text
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        #pyray.draw_text(image, x, y, font_size, color) # This will just draw the text of the path to the image
        
    def draw_actors(self, actors):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    #This was also found in Batter (below, which I commented out)
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def get_cell_size(self):
        """Gets the video screen's cell size.
        
        Returns:
            Grid: The video screen's cell size.
        """
        return self._cell_size

    def get_height(self):
        """Gets the video screen's height.
        
        Returns:
            Grid: The video screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width

    #This was also found in Batter (below, which I commented out)
    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
    
    
    
    #Originally from Batter
    """A video service inteface."""

    #def clear_buffer(self): # Had to comment out for RFK
        #"""Prepares the buffer for drawing."""
        #raise NotImplementedError("not implemented in base class")

    def draw_image(self, image, position):
        """Draws the given image on the buffer at the given position. The image won't appear
        on the screen until flush_buffer() is called.

        Args:
            image: An instance of batter.casting.image.
            position: An instance of batter.casting.point.

        Raises:
            KeyError: If the image file hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_rectangle(self, size, position, color):
        """Draws a rectangle on the buffer at the given position. The rectangle won't appear
        on the screen until flush_buffer() is called.

        Args:
            size: An instance of batter.casting.point.
            position: An instance of batter.casting.point.
            color: An instance of batter.casting.color.
        """
        raise NotImplementedError("not implemented in base class")

    def draw_text(self, text, position):
        """Draws the given text on the buffer at the given position. The text won't appear
        on the screen until flush_buffer() is called.

        Args:
            text: An instance of batter.casting.text.
            position: An instance of batter.casting.point.

        Raises:
            KeyError: If the font file for the text hasn't already been loaded.
        """
        raise NotImplementedError("not implemented in base class")

    #def flush_buffer(self): # Had to comment out for RFK
    #    """Swaps the buffers, displaying everything that has been drawn on the screen."""
    #    raise NotImplementedError("not implemented in base class")

    def initialize(self):
        """Initializes underlying video device. This method should be called before the main game 
        loop begins."""
        raise NotImplementedError("not implemented in base class")

    #def is_window_open(self): # Had to comment out for RFK
    #   """Wether or not the window is open.
    #   
    #   Returns:
    #       True if the window is open; false if otherwise.
    #   """
    #    raise NotImplementedError("not implemented in base class")

    def load_fonts(self, directory):
        """Loads all the fonts in the given directory and sub-directories.
        
        Args:
            directory: A string containing the absolute folder path where font files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def load_images(self, directory):
        """Loads all the images in the given directory and sub-directories.
        
        Args:
            directory: A string containing the absolute folder path where image files are stored.
        """
        raise NotImplementedError("not implemented in base class")

    def release(self):
        """Releases the underlying video device. This method should be called after the game loop 
        has finished running."""
        raise NotImplementedError("not implemented in base class")

    def unload_fonts(self):
        """Unloads all fonts that were previously loaded."""
        raise NotImplementedError("not implemented in base class")

    def unload_images(self):
        """Unloads all images that were previously loaded."""
        raise NotImplementedError("not implemented in base class")