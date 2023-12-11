import os
from typing import Any
import pygame
from pygame.locals import *

main_dir = os.path.dirname(__file__)
images_dir = os.path.join(main_dir, "images")
sprite_dir = os.path.join(images_dir, 'pacman_sprite.png')

print(sprite_dir)

class buballo(pygame.sprite.Sprite):

    def update():
