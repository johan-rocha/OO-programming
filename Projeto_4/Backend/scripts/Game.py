#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

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
        self._font = pygame.font.SysFont('liberationmono', 30, True, False)#config text #verify fonts: pygame.font.get_fonts()
        pygame.display.set_caption("FGA-PACMAN")#ver se esta correto

        self._sprite_sheet = pygame.image.load(os.path.join(constants.IMAGE_DIR, constants.SPRITE_SHEET))

        self.__running = True
        self.__lives = 3
        self.__pacman = Pacman(nickname, self.__screen, self._sprite_sheet) #definir parametros
        self.__pellets = Pellets() #definir parametros
        self.__ghost = Ghost(constants.INKY, self.__screen, self._sprite_sheet) #transformar em lista
        self.__score = 0
        self.__timer = 0

    def newGame(self):
        self._all_sprites = pygame.sprite.Group()
        self._all_sprites.add(self.__pacman)
        self._all_sprites.add(self.__ghost) #isso esta dando erro
        self.startGame()
    
    def startGame(self) -> None:
        self.runGame() # so para testes, arrumar

    def reset(self) -> None:
        pass

    def gameOver(self) -> None:
        self.__playing = False
    
    def runGame(self):
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
                    self.__pacman.setDirection(constants.LEFT)
                if event.key == pygame.K_w:        
                    self.__pacman.setDirection(constants.UP)
                if event.key == pygame.K_d:
                    self.__pacman.setDirection(constants.RIGHT)
                    self.__ghost.preyMode() #teste
                if event.key == pygame.K_s:
                    self.__pacman.setDirection(constants.DOWN)

            #o controle de ghost eh feito pela IA
    
    def itsRunning(self) -> bool:
        return self.__running

    def pelletsEaten() -> int:
        pass

    def waitForUser() -> None:
        pass
    
    def collided() -> bool:
        pass

    def eatGhost() -> None:
        pass
    
    def dead(self) -> None:
        if(self.__lives):
            self.decrementLives()
        else:
            self.gameOver()

    def decrementLives(self) -> None:
        self.__lives -= 1

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
        self.__ghost.move()
        """ for ghost in self.__ghost:
            pass """

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


