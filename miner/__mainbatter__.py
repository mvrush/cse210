from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager

from game.services.keyboard_service import KeyboardService # Had to import the keyboard service to send it from here to the RFK merged director

keyboard_service = KeyboardService(CELL_SIZE)
cast = "" # I have to define cast so we can pass it below
def main():
    director = Director(SceneManager.VIDEO_SERVICE, keyboard_service) # Here I am passing both the VIDEO_SERVICE and KEYBOARD_SERVICE variables from SceneManager
    director.start_game(cast) # We have to pass 'cast' because I'm using the RFK director merged with Batter. If I don't pass it, the game crashes.

if __name__ == "__main__":
    main()