from constants import *
from game.scripting.action import Action


class MoveBallAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity) # Removed this to stop the ball from moving on it's own

        body.set_position(position) # This was already in MoveBallAction
