import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Miner"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/batter/assets/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banners
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0)) # Sets X to CELL_SIZE(15) and Y to 0 for placement in top left corner
    cast.add_actor("banners", banner)

    banner_gold = Actor()
    banner_gold.set_text("Gold: 0")
    banner_gold.set_font_size(FONT_SIZE)
    banner_gold.set_color(WHITE)
    banner_gold.set_position(Point(CELL_SIZE, CELL_SIZE * 1)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *1(15)
    cast.add_actor("banners", banner_gold)

    banner_silver = Actor()
    banner_silver.set_text("Silver: 0")
    banner_silver.set_font_size(FONT_SIZE)
    banner_silver.set_color(WHITE)
    banner_silver.set_position(Point(CELL_SIZE, CELL_SIZE * 2)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *2(30)
    cast.add_actor("banners", banner_silver)

    banner_coal = Actor()
    banner_coal.set_text("Coal: 0")
    banner_coal.set_font_size(FONT_SIZE)
    banner_coal.set_color(WHITE)
    banner_coal.set_position(Point(CELL_SIZE, CELL_SIZE * 3)) # Sets X to CELL_SIZE(15) and Y to CELL_SIZE *2(45)
    cast.add_actor("banners", banner_coal)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.randint(33, 126))
        message = messages[n] # Message will tell user what they found

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()