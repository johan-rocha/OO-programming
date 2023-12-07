import abc #Abstract Base Classes
import pygame
from pygame.locals import *



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
    def __init__(self, surface: pygame.Surface):
        self.__x_pacman = surface.get_width()/2
        self.__y_pacman = surface.get_height()/2 #initial position / TALVEZ APAGAR
        self.__pacman_geometry = pygame.draw.circle(surface, self._color, (self.__x_pacman, self.__y_pacman), 12) #muito provavel de apagar
        self._color = (244, 206, 14)

    def move(self) -> None:
        if(self._direction == -1):
            pass
        elif(self._direction == 0):
            self.__x_pacman -= self._speed
            self.__y_pacman = 0
        elif(self._direction == 1):
            self.__y_pacman -= self._speed
            self.__x_pacman = 0
        elif(self._direction == 2):
            self.__x_pacman += self._speed
            self.__y_pacman = 0
        elif(self._direction == 3):
            self.__y_pacman += self._speed
            self.__x_pacman = 0

    @property
    def getGeometry(self):
        return self.__pacman_geometry

    @getGeometry.setter
    def setGeometry(self, surface: pygame.Surface, radius: float=12):
        self.__pacman_geometry = pygame.draw.circle(surface, self._color, (self.__x_pacman, self.__y_pacman), radius)

    @property
    def getDirection(self):
        return self._direction
    
    @getDirection.setter
    def setDirection(self, value):
        self._direction = value

class Ghost(Characters): #definir classe
    def __init__(self):
        pass