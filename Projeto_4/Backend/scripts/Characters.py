import abc #Abstract Base Classes
import pygame
from pygame.locals import *
from pygame.surface import Surface



class Characters(abc.ABC): #abstract class
    #speed
    #name
    #color
    
    @abc.abstractmethod
    def __init__(self, speed=10, color=(0, 0, 0), direction=-1):
        self._speed = speed #default
        self._color = color
        self._direction = direction #TALVEZ APAGAR

    #ver como funciona, usando como exemplo
    def setSpeed(self, value):
        self._speed = value

class Pacman(Characters): #definir classe
    def __init__(self, surf: Surface):
        super().__init__()
        self.__surface = surf
        self.__x_pacman = surf.get_width()/2
        self.__y_pacman = surf.get_height()/2 #initial position / TALVEZ APAGAR
        self.pacman_ref_geometry = 0 #muito provavel de apagar
        self._color = (244, 206, 14)

    def move(self) -> None:
        if(self._direction == -1):
            pass
        elif(self._direction == 0):
            self.__x_pacman -= self._speed
        elif(self._direction == 1):
            self.__y_pacman -= self._speed
        elif(self._direction == 2):
            self.__x_pacman += self._speed
        elif(self._direction == 3):
            self.__y_pacman += self._speed
        self.__x_pacman %= self.__surface.get_width() #teleport character
        self.__y_pacman %= self.__surface.get_height()

    def getPosition(self):
        return self.__x_pacman, self.__y_pacman
    
    def getColor(self):
        return self._color

    def getDirection(self):
        return self._direction
    
    def setDirection(self, value):
        self._direction = value

class Ghost(Characters): #definir classe
    def __init__(self):
        pass