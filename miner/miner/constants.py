import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Miner"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
#FONT_FILE = "batter/assets/fonts/zorque.otf" # Have to remove 'batter/' from the path because we are starting in the 'batter' folder already.
FONT_FILE = "batter/assets/fonts/RubikGemstones-Regular.ttf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "batter/assets/sounds/mineral.wav"
WELCOME_SOUND = "batter/assets/sounds/ready.wav"
OVER_SOUND = "batter/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
BROWN = Color(89, 55, 4)

# KEYS
LEFT = "left"
RIGHT = "right"
UP = "up" # Add key from the raylib_keyboard_service.py for up movement.
DOWN = "down" # Add key from the raylib_keyboard_service.py for down movement.
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
#LEVEL_FILE = "batter/assets/data/level-{:03}.txt" # Need to take 'batter/' off this path since that's the directory we're starting from
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
#BALL_IMAGE = "batter/assets/images/000.png"
BALL_IMAGE = "batter/assets/images/wega.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "rackets" # This is now our miner
RACKET_IMAGES = [f"batter/assets/images/{n:03}.png" for n in range(100, 103)]
#RACKET_IMAGES = "batter/assets/images/miner.png" # Load the image of the miner. I tried to do this with a single image and couldn't.
RACKET_WIDTH = 28 # This was 106 and I changed it to 28 to match the size of the ball
RACKET_HEIGHT = 28 * 2.5 # Had to 2.5 times the height of the racket to fit the whole miner img.
RACKET_RATE = 6 # how quickly it goes through the animations to form the animation speed of the pick.
RACKET_VELOCITY = 3 # How fast the miner moves on the screen

# BRICK
BRICK_GROUP = "bricks"
BRICK_IMAGES = {
    "b": [f"batter/assets/images/{i:03}.png" for i in range(10,19)], # {i:03}.png means first 3 letters before the .png for the filename. To animate you put the row and number of animation images in the data text file. To go through all 9 images you would put 'b9' to just to one image you do 'b1'
    "g": [f"batter/assets/images/{i:03}.png" for i in range(20,29)],
    "p": [f"batter/assets/images/{i:03}.png" for i in range(30,39)],
    "y": [f"batter/assets/images/{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 80 # Increase height from 28 to 80 to space minerals per their size.
BRICK_DELAY = 0.5 # The delay between animation sequences
BRICK_RATE = 4 # how quickly it goes through the images to form the animation speed.
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "GET READY TO MINE!"
WAS_GOOD_GAME = "GAME OVER"