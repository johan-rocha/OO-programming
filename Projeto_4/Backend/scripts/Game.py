#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pygame
from Characters import *
from sys import exit
import os
import numpy as np
import constants

class Game():

    def __init__(self, nickname : str):

        pygame.init()
        pygame.font.init()
        
        self.__screen = pygame.display.set_mode((constants.WIDTH*constants.SCALE, constants.HEIGHT*constants.SCALE+constants.SCOREBOARD_RECOIL*constants.SCALE))
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
        self._all_sprites.add(self.__ghost)
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
        self.backGroundPacman(constants.BACKGROUND_PLAYING)
        self._all_sprites.draw(self.__screen)
        self._all_sprites.update()

    def updateObjMovGame(self) -> None:
        self.__pacman.move()
        self.__ghost.move()
        """ for ghost in self.__ghost:
            pass """

    def updateTexts(self):
        pass #configurar uma classe para textos e criar um vetor de textos para serem atualizados

    def backGroundPacman(self, mode):
        if(mode == constants.BACKGROUND_PLAYING):
            self.__background = self._sprite_sheet.subsurface((228,0), (224, 248))
        else:
            self.__background = self._sprite_sheet.subsurface((0,0), (224, 248))

        self.__background = pygame.transform.scale(self.__background, (224*constants.SCALE, 248*constants.SCALE))
        self.__screen.blit(self.__background, (0,0))

class Pellets(): #definir classe
    def __init__(self):
        pass

class Map(pygame.sprite.Sprite, GameSprites): #modificar para numpy
    def __init__(self):
        self.matriz_width = int(constants.WIDTH/4)
        self.matriz_height = int(constants.HEIGHT/4)
        self.block = np.ones((int(4 * constants.SCALE), int(4 * constants.SCALE)), dtype=int)
        self.__matriz_map_colision = np.zeros((self.matriz_height, self.matriz_width), dtype=int)
        self.initMap()

    def initMap(self):
        for i in range(20):
            self.__matriz_map_colision[i, 0] = 1
            self.__matriz_map_colision[i, self.matriz_width-1] = 1

        for i in range(38, self.matriz_height):
            self.__matriz_map_colision[i, 0] = 1
            self.__matriz_map_colision[i, self.matriz_width-1] = 1

        for i in range(20, 26): #correto
            self.__matriz_map_colision[i, 10] = 1
            self.__matriz_map_colision[i, (self.matriz_width-1)-10] = 1
            self.__matriz_map_colision[i+12, 10] = 1 #i + ...
            self.__matriz_map_colision[i+12, (self.matriz_width-1)-10] = 1

        for j in range(self.matriz_width):
            self.__matriz_map_colision[0, j] = 1
            self.__matriz_map_colision[self.matriz_height-1, j] = 1

        for j in range(11): #correto
            self.__matriz_map_colision[19, j] = 1 #
            self.__matriz_map_colision[19, (self.matriz_width-1)-j] = 1
            self.__matriz_map_colision[26, j] = 1 #
            self.__matriz_map_colision[26, (self.matriz_width-1)-j] = 1
            self.__matriz_map_colision[31, j] = 1 #
            self.__matriz_map_colision[31, (self.matriz_width-1)-j] = 1
            self.__matriz_map_colision[38, j] = 1 #
            self.__matriz_map_colision[38, (self.matriz_width-1)-j] = 1
    
    def checkColision(self, obj_position : tuple[int, int]):
        pass


#map tem que ter o background e as colisoes

"""
obs: quando herdar e o metodo tiver o mesmo nome, inclusive o construtor, deve conter super()
   
 ex:
    
    def super().__init__(self):
 
 """



g = Game("fraldinha")

while g.itsRunning():
    g.newGame()


