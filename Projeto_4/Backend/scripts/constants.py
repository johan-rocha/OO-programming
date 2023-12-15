import os

# SCREEN DIMENSIONS
WIDTH = 452
HEIGHT = 516

#FOLDERS
IMAGE_DIR = os.path.join(os.getcwd(), "images")
SOUND_DIR = os.path.join(os.getcwd(), "sounds")

#SPRITE SHEET
SPRITE_SHEET = 'pacman_sprite.png'

#LOGO
PACMAN_LOGO = 'pacman_logo.png'

#COLORS
BLACK = (0, 0 ,0)

#FRAME RATE
FPS = 60

#GHOSTS
CLYDE = 0
INKY = 1
PINKY = 2
BLINKY = 3

#FACTOR SPEED SPRITE (0.1 -> 0.9)
FACTOR_SPEED_SPRITE = 1.5