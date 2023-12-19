import pygame
from Characters import GameSprites
import constants
import numpy as np

class Map(pygame.sprite.Sprite, GameSprites): #modificar para numpy
    def __init__(self):
        self.initMap()

    def initMap(self):
        pass
    
    def checkColision(self, obj_position : tuple[int, int]):
        #multiplicar constants.WIDTH por constants.SCALE
        with open("map.bin", 'rb') as file:
            file.seek((obj_position[0] * constants.WIDTH + obj_position[1]) * np.dtype(int).itemsize)
            estado_colisao = np.fromfile(file, dtype=int, count=1)
        return estado_colisao