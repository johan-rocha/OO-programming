import os

# SCREEN DIMENSIONS
SCALE = 2
WIDTH = 224
HEIGHT = 248
SCOREBOARD_RECOIL = 50

#FOLDERS
IMAGE_DIR = os.path.join(os.getcwd(), "images")
SOUND_DIR = os.path.join(os.getcwd(), "sounds")

#SPRITE SHEET
SPRITE_SHEET = 'pacman_sprite.png'

#LOGO
PACMAN_LOGO = 'pacman_logo.png'

#COLORS
BLACK = (0, 0 ,0)
RED = (255, 0, 0)

#FRAME RATE
FPS = 100

#GHOSTS
CLYDE = 0
INKY = 1
PINKY = 2
BLINKY = 3

#FACTOR SPEED SPRITE (1(speed) -> 2(low))
FACTOR_SPEED_SPRITE_PACMAN = 2.5 * SCALE
FACTOR_SPEED_SPRITE_GHOST = 10 * SCALE

#GHOST STATES
ALIVE = 0
PREY = 1
DIE = 2

#SENTIDOS
LEFT = 0
UP = 1
RIGHT = 2
DOWN = 3

#DEFAULT SPEED
DEFAULT_SPEED = 1 #original = 2.5

#BACKGROUND MODE
BACKGROUND_INICIALIZE = 0
BACKGROUND_PLAYING = 1