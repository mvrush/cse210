from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        # food = cast.get_first_actor("foods") # Removed for Cycle. Don't need food
        snake = cast.get_first_actor("cycles") # gets thr first actor from the 'cycles' group. 'cycles' is passed to the 'get_first_actor(group)' method found in Cast() class.
        segments = snake.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        #self._video_service.draw_actor(food) # Removed for Cycle. Don't need food.
        self._video_service.draw_actors(segments)
        snake.grow_tail(1) # # uses our instance of 'cast.get_first_actor("cycles")' held in the 'snake' variable and calls the 'grow_tail()' method there. I specified 1 to grow the tail 1 length.
        self._video_service.draw_actor(score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()