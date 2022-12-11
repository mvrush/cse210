from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            racket.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket.swing_right()
        ### Added the next 2 elif statements to move the racket up and down
        elif self._keyboard_service.is_key_down(UP): 
            racket.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            racket.swing_down()
        
    
        else: 
            racket.stop_moving()        