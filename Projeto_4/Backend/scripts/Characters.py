import abc #Abstract Base Classes
import pygame
from pygame.locals import *
from pygame.surface import Surface



class Characters(abc.ABC): #abstract class
    
    @abc.abstractmethod
    def __init__(self, init_coord : list, surface : Surface, speed=10, color=(0, 0, 0), direction=-1):
        self.__speed = speed #default
        self.__color = color
        self.__direction = direction #TALVEZ APAGAR
        self.__coordinates = init_coord
        self.__surface = surface
        self.ref_geometry = 0 #muito provavel de apagar

    def move(self) -> None:
        if(self.__direction == -1):
            pass
        elif(self.__direction == 0):
            self.__coordinates[0] -= self.__speed
        elif(self.__direction == 1):
            self.__coordinates[1] -= self.__speed
        elif(self.__direction == 2):
            self.__coordinates[0] += self.__speed
        elif(self.__direction == 3):
            self.__coordinates[1] += self.__speed
        self.__coordinates[0] %= self.__surface.get_width() #teleport character
        self.__coordinates[1] %= self.__surface.get_height()

    #ver como funciona, usando como exemplo
    def setSpeed(self, value):
        self.__speed = value

    def getDirection(self):
        return self.__direction
    
    def setDirection(self, value):
        self.__direction = value

    def getColor(self):
        return tuple(self.__color)
    
    def setColor(self, value : list):
        self.__color = value
    
    def getPosition(self):
        return self.__coordinates[0], self.__coordinates[1]

class Pacman(Characters): #definir classe
    def __init__(self, nickname : str, surf: Surface):
        self.__x_pacman = surf.get_width()/2 + 200
        self.__y_pacman = surf.get_height()/2 + 200 #initial position / TALVEZ APAGAR
        super().__init__([self.__x_pacman, self.__y_pacman], surf, 10, (244, 206, 14))

        self.__has_power = False
        self.__nickname = nickname
    
    def die():
        pass

    def incrementPelletsEaten():
        pass

    def defineHasPower():
        pass

class Ghost(Characters): #definir classe
    def __init__(self, surf: Surface, color : tuple):
        self.__x_ghost = surf.get_width()/2
        self.__y_ghost = surf.get_width()/2
        super().__init__([self.__x_ghost, self.__y_ghost], surf, 10, color)

        self.__ghost_value = 0
        self.setDirection(1)

    def respawn():
        pass

    def arrayList():
        pass

    def behavior():
        pass
