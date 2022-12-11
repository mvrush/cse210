from constants import *
from game.scripting.action import Action


class DrawBricksAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        
        for brick in bricks:
            body = brick.get_body() # It goes through the following properties and adds them to create the brick body (unless it's in debug mode)

            if brick.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = brick.get_animation()
            image = animation.next_image() # This is used by the 'scene_manager.py'. All these things are part of the brick body.
            position = body.get_position()
            self._video_service.draw_image(image, position)