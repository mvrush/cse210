from game.casting.scoring import Scoring

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._scoring = Scoring() # This intantiates an instance of the 'Scoring()' class so we can access it's methods and variables
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_single_actor("robots", 0)
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_single_actor("banners", 0)
        banner_gold = cast.get_single_actor("banners", 1) # Will need to overwrite these with 'set_text()' like we do for the main banner when we score
        banner_silver = cast.get_single_actor("banners", 2)
        banner_coal = cast.get_single_actor("banners", 3)
        robot = cast.get_single_actor("robots", 0)
        artifacts = cast.get_actors("artifacts") # The artifacts are coming from our instance of 'cast' passed from '__main__.py'

        # Set the text for the banners. None for message text, current score for the other three.
        #banner.set_text("") # I don't have to do this everytime because I don't want the banner erased each time through.
        banner_gold.set_text(f"Gold: {self._scoring.get_score('gold')}") # We created the Gold banner in __main__.py but we'll need to overwrite it with the calculated score like we did in Greed but using the same method we write the banner text.
        banner_silver.set_text(f"Silver: {self._scoring.get_score('silver')}")
        banner_coal.set_text(f"Coal: {self._scoring.get_score('coal')}")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message() # Gets the 'message' value for the artifact, assigns it to the 'message' variable
                text = artifact.get_text() # Gets the 'text' value for the artifact, assigns it to the 'text' variable. Text will hold either 'G', 'S', or 'C'.
                score = artifact.get_value() # Gets the 'value' value for the artifact and assigns it to the 'score' variable
                banner.set_text(message)
                self._scoring.set_score(text, score)  # Call instance of Scoring() class, use 'set_score()' method and passes it the value of the artifact using the 'score' variable
                cast.remove_actor("artifacts", artifact) # After banner is set and score is set, it removes the artifact. If I don't do this, it rolls up the score during each frame refresh.
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()