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
MAX_X = 900 # This is the maximum x (horizontal) width of the screen
MAX_Y = 600 # This is the maximum y (vertical) height of the screen
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60 # This splits the width (x) into 60 columns
ROWS = 40 # This splits the height (y) into 40 rows
CAPTION = "Greed" # The caption written at the top of our window that the game opens
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt" # path to our data file
WHITE = Color(255, 255, 255) # Defines the color white
DEFAULT_ARTIFACTS = 40 # the number of artifacts we show on the screen.


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    # the following lines position our robot.
    x = int(MAX_X / 2) # This takes the MAX_X value listed above and divides it by two. That places it right in the middle.
    # 'y' variable takes the MAX_Y value listed above and divides it by -40. That places it at the bottom. 
    # I don't know why this math works. I think it has something to do with the ROW value but not sure.
    y = int(MAX_Y / -40)
    position = Point(x, y) # the 'position' for the robot is the Point() values for x and y we just defined right above.

    # Calls the Actor() class, instantiates it as 'robot' and sets the values from the Actor() class using it's methods
    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read() # reads the data from our data file
        messages = data.splitlines() # We won't be using messages anymore but this splits each line into it's own list (array) item

    for n in range(DEFAULT_ARTIFACTS): # This 'for' loop loops through the 40 artifacts and creates them.
        #text = chr(random.choice([42, 48])) # This line uses the random.choice() function to choose between the unicode characters 42=* and 48=0 and populate the artifacts.
        text = random.choice(['*', '0']) # This line uses the random.choice() function to choose between the string '*' or '0' {zero}.
        message = messages[n] # We won't be using messages anymore

        x = random.randint(1, COLS - 1) # This sets a random value for our x (horizontal) position in the columns
        y = random.randint(1, ROWS - 1) # This sets a random value for our y (vertical) position in the rows
        position = Point(x, y) # this will be the position for one artifact as it loopws.
        position = position.scale(CELL_SIZE) # sets the position size to equal what we defined for our CELL_SIZE

        # The next 4 lines create a random color for each artifact
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # Calls our Artifact() class and sets each of the values below using the methods in the Artifact() class
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message) # We don't need a message anymore.
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()