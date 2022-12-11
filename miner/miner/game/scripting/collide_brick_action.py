from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        miner = cast.get_first_actor(RACKET_GROUP) # We're still using our Racket as the miner but here I've given it the 'miner' variable.
        stats = cast.get_first_actor(STATS_GROUP)
        
        for brick in bricks:
            ball_body = ball.get_body() # Won't be using this as the subject anymore because we got rid of the ball.
            brick_body = brick.get_body()
            miner_body = miner.get_body() # We pull the body info of 'miner' (which is actually from the RACKET_GROUP) and hold it in the 'miner_body' variable.

            if self._physics_service.has_collided(miner_body, brick_body): # We pass the subject and agent to the 'has_collided()' function to determine if the subject has collided with the agent.
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)