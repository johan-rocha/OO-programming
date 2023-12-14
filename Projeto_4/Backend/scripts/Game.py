#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import time #verificar funcionamento dessa funcao
import pygame
from Characters import *
from sys import exit
import os
import constants

class Game():

    def __init__(self, nickname : str):

        pygame.init()
        pygame.font.init()


        self.__screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.__clock = pygame.time.Clock()
        self._font = pygame.font.SysFont('liberationmono', 30, True, False)#config text
#verify fonts: pygame.font.get_fonts()
        pygame.display.set_caption("FGA-PACMAN")#ver se esta correto





        self.__lives = 3
        self.__pacman = Pacman(nickname, self._screen, self._sprite_sheet) #definir parametros
        self.__pellets = Pellets() #definir parametros
        self.__ghost = [] #configurar primeiro a classe ghost para instanciar
        self.__score = 0
        self.__timer = 0
        self.__attribute20 = 0

    def newGame(self):
        #instancia as classes das sprites
        self._sprite_sheet = pygame.image.load(os.path.join(constants.IMAGE_DIR, 'pacman_sprite.png')).convert_alpha()

        self._all_sprites = pygame.sprite.Group()
    
    def runGame(self):
        self.__running = True
        self.__playing = True
        while self.__playing:
            self.__clock.tick(constants.FPS) #frame rate
            self.controls()
            self.updateObjMovGame()
            self.updateSprites()
            self.updateTexts()
            pygame.display.flip()
        pygame.quit()
        exit()



    def controls(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__playing = False
                self.__running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.__pacman.setDirection(0)
                if event.key == pygame.K_w:        
                    self.__pacman.setDirection(1)
                if event.key == pygame.K_d:
                    self.__pacman.setDirection(2)
                if event.key == pygame.K_s:
                    self.__pacman.setDirection(3)

            #adicionar algoritmo de controle dos fantasmas
    
    def itsRunning(self) -> bool:
        return self.__running


    def pelletsEaten() -> int:
        pass

    def startGame() -> None:
        pass

    def reset() -> None:
        pass

    def gameOver() -> None:
        pass
    
    def collided() -> bool:
        pass

    def eatGhost() -> None:
        pass
    
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

    def updateSprites(self):
        self.__screen.fill(constants.BLACK)
        self._all_sprites.draw(self.__screen)
        self._all_sprites.update()

    def updateObjMovGame(self) -> None:
        self.__pacman.move()
        for ghost in self.__ghost:
            ghost.move()

    def updateTexts(self):
        pass #configurar uma classe para textos e criar um vetor de textos para serem atualizados


class Pellets(): #definir classe
    def __init__(self):
        pass

"""
obs: quando herdar e o metodo tiver o mesmo nome, inclusive o construtor, deve conter super()
   
 ex:
    
    def super().__init__(self):
 
 """



g = Game("fraldinha")

while g.itsRunning():
    g.newGame()


