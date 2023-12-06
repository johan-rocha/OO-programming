#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time #verificar funcionamento dessa funcao
import pygame
from pygame.locals import *
from sys import exit

class Game():

    def __init__(self):
        self.lives = 3
        pellets = Pellets() #definir parametros
        pacman = Pacman() #definir parametros
        ghost = []
        score = 0
        timer = 0
        attribute20 = 0
    
    def move() -> None:
        pass
    
    def pelletsEaten() -> int:
        pass

    def startGame() -> None:
        pass

    def reset() -> None:
        pass
    
    def collided() -> bool:
        pass

    def eatGhost() -> None:
        pass
    
    @property
    def dead() -> None:
        pass

    def decrementLives() -> None:
        pass

    def eatPellets() -> None:
        pass
    
    def incrementPelletsEaten() -> None:
        pass

    def getScore() -> int:
        pass

    def incrementScore() -> None:
        pass

    def updateGame() -> None:
        pass

    def gameOver() -> None:
        pass

class Pellets(): #definir classe
    def __init__(self):
        pass

"""
obs: quando herdar e o metodo tiver o mesmo nome, inclusive o construtor, deve conter super()
   
 ex:
    
    def super().__init__(self):
 
 """