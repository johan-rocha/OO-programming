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
        self.__pacman = Pacman("Johan", self.__screen, self._sprite_sheet) #definir parametros
        self.__pellets = Pellets() #definir parametros
        self.__ghost = []
        self.__ghost.append(Ghost(constants.CLYDE, self.__screen, self._sprite_sheet))
        self.__ghost.append(Ghost(constants.INKY, self.__screen, self._sprite_sheet))
        self.__ghost.append(Ghost(constants.PINKY, self.__screen, self._sprite_sheet))
        self.__ghost.append(Ghost(constants.BLINKY, self.__screen, self._sprite_sheet))
        self.__score = 0
        self.__timer = 0

    def newGame(self):
        self._ghosts_sprites = pygame.sprite.Group()

        count = 90*constants.SCALE
        for ghost in self.__ghost:
            self._ghosts_sprites.add(ghost)
            ghost.setPosition((count ,91*constants.SCALE))
            count += 18*constants.SCALE

        self._pacman_sprites = pygame.sprite.Group()
        self._pacman_sprites.add(self.__pacman)
        self.__pellets.setPellets()
        self.startGame()
    
    def startGame(self) -> None:
        self.runGame() # so para testes, arrumar

    def reset(self) -> None:
        pass

    def gameOver(self) -> None:
        self.__playing = False
        print("GAME OVER!")
    
    def runGame(self):
        self.__playing = True
        while self.__playing:
            self.__clock.tick(constants.FPS) #frame rate
            self.controls()
            self.updateObjMovGame()
            self.ghostCollided()
            self.updateSprites()
            #pygame.draw.rect(self.__screen, constants.RED, self.__pacman.b_box_colision, 2) #FOR TEST
            self.updateTexts()
            pygame.display.flip()
        pygame.quit()
        exit()


    def controls(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__playing = False
                self.__running = False

            if(not self.__pacman.getPacmanIsDead()):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.__ghost[0].setDirection(constants.LEFT)
                    if event.key == pygame.K_w:        
                        self.__ghost[0].setDirection(constants.UP)
                    if event.key == pygame.K_d:
                        self.__ghost[0].setDirection(constants.RIGHT)
                    if event.key == pygame.K_s:
                        self.__ghost[0].setDirection(constants.DOWN)

                    if event.key == pygame.K_LEFT:
                        self.__pacman.setDirection(constants.LEFT)
                    if event.key == pygame.K_UP:        
                        self.__pacman.setDirection(constants.UP)
                    if event.key == pygame.K_RIGHT:
                        self.__pacman.setDirection(constants.RIGHT)
                    if event.key == pygame.K_DOWN:
                        self.__pacman.setDirection(constants.DOWN)

            #o controle de ghost eh feito pela IA
    
    def itsRunning(self) -> bool:
        return self.__running

    def pelletsEaten(self) -> int:
        for pellet in self.__pellets.objs:
            pygame.draw.rect(self.__screen, constants.PINK, pellet, 2)
            if(pellet.colliderect(self.__pacman.rect)):
                if(not self.__pacman.getHasPower()):
                    self.__score += 10 
                else:
                    self.__score += 20#colocar som comendo aqui
                self.__pellets.objs.remove(pellet)
                continue
        for power in self.__pellets.powerObjs:
            pygame.draw.rect(self.__screen, constants.PINK, power, 0)
            if(power.colliderect(self.__pacman.rect)):
                for ghost in self.__ghost:
                    ghost.preyMode()
                self.__pacman.defineHasPower()
                self.__score += 20 #colocar som comendo aqui
                self.__pellets.powerObjs.remove(power)
                continue

    def waitForUser() -> None:
        pass
    
    def ghostCollided(self) -> bool:
        for ghost in self.__ghost:        
            if(pygame.sprite.spritecollide(self.__pacman, self._ghosts_sprites, False)):
                #se ghost_state = ALIVE -> pacman morre
                #se ghost_state = PREY -> aumenta 2000 pontos e o ghost morre (eatGhost)
                if(ghost.getGhostState() == constants.ALIVE and
                (not self.__pacman.getPacmanIsDead())):
                    self.dead()
                    return True
    
    def dead(self) -> None:
        if(self.__lives):
            #jogo para
            self.decrementLives()
            self.__pacman.dieMode()
            self.__pacman.setDirection(-1)
            for ghost in self.__ghost:
                ghost.setDirection(-1)
            self.respawn()
            #voltam para posicao inicial
        else:
            pass
            self.gameOver() #consertar, tá colidindo varias vezes e chamando gameover

    def decrementLives(self) -> None:
        self.__lives -= 1

    def eatGhost() -> None:
        pass

    def respawn(self):
        self.__pacman.setPosition((112*constants.SCALE, 139*constants.SCALE))
        count = 90*constants.SCALE
        for ghost in self.__ghost:
            ghost.setPosition((count ,91*constants.SCALE))
            count += 18*constants.SCALE
        self.__pacman.eatMode()
    
    def incrementPelletsEaten() -> None: #serve para verificar se o jogador venceu o jogo
        pass

    def getScore() -> int:
        pass

    def incrementScore() -> None:
        pass

    def updateSprites(self):
        self.__screen.fill(constants.BLACK)
        self.backGroundPacman(constants.BACKGROUND_PLAYING)
        self.pelletsEaten()
        self._pacman_sprites.draw(self.__screen)
        self._ghosts_sprites.draw(self.__screen)
        self._pacman_sprites.update()
        self._ghosts_sprites.update()

    def updateObjMovGame(self) -> None:
        self.__pacman.move()
        for ghost in self.__ghost:
            ghost.move()

    def updateTexts(self):
        message = f"SCORE = {self.__score}"
        formated_message = self._font.render(message, True, (255, 255, 255))
        self.__screen.blit(formated_message, 
                           (22*constants.SCALE, 248*constants.SCALE + 30*constants.SCALE)
                           )

    def backGroundPacman(self, mode):
        if(mode == constants.BACKGROUND_PLAYING):
            self.__background = self._sprite_sheet.subsurface((228,0), (224, 248))
        else:
            self.__background = self._sprite_sheet.subsurface((0,0), (224, 248))

        self.__background = pygame.transform.scale(self.__background, (224*constants.SCALE, 248*constants.SCALE))
        self.__screen.blit(self.__background, (0,0))











class Pellets():
    def __init__(self):
        self.__total_pellets = 0
        self.objs = []
        self.powerObjs = []
    
    def setPellets(self):
        x_count = 0
        y_count = 10
        
        for y in range(constants.HEIGHT*constants.SCALE):# Fill available route
            top_points = (y < 70*constants.SCALE)
            bottom_points = (y > 161*constants.SCALE)

            y_count %= 8*constants.SCALE
            x_count = y_count
            for x in range(constants.WIDTH*constants.SCALE//2):
                central_points = (y > 72*constants.SCALE and
                                   y < 160*constants.SCALE 
                                   and x == 51*constants.SCALE)

                if(top_points or bottom_points or central_points): #colocar as condições centrais depois
                    if(not self.__outMap((x, y))):
                        x_count %= 8*constants.SCALE
                        if((x_count == 0)): # and not self.__ocuppiedPosition(x, y)
                            self.__putPellet((x,y))
                        x_count+=1
            y_count += 1
        self.__total_pellets = len(self.objs)
    
    def __outMap(self, obj_position : tuple[int, int]):
        
        col, row = int(obj_position[0]), (obj_position[1])
        position = int(row * constants.WIDTH*constants.SCALE + col)
        offset = int(position * np.dtype(int).itemsize)

        with open("map.bin", 'rb') as file:
            file.seek(offset)
            estado_colisao = np.fromfile(file, dtype=int, count=1)
        return estado_colisao.item()
    
    def __putPellet(self, insert_point : tuple[int, int]):
        x_mirror, y = insert_point
        x_mirror = constants.SCALE*constants.WIDTH - x_mirror
        power_pellet_pos = (insert_point == (11*constants.SCALE,27*constants.SCALE) or
                             insert_point == (11*constants.SCALE,187*constants.SCALE))

        if(not power_pellet_pos):
            rect = pygame.Rect(insert_point, (2*constants.SCALE,2*constants.SCALE))
            mirror_rect = pygame.Rect(insert_point, (2*constants.SCALE,2*constants.SCALE))
            mirror_rect.topright = x_mirror, y
            self.objs.append(rect)
            self.objs.append(mirror_rect)
        else:
            insert_point_with_offset = insert_point[0]-3*constants.SCALE, insert_point[1]-3*constants.SCALE

            rect = pygame.Rect(insert_point_with_offset, (8*constants.SCALE,8*constants.SCALE))
            mirror_rect = pygame.Rect(insert_point, (8*constants.SCALE,8*constants.SCALE))
            mirror_rect.topright = x_mirror+3*constants.SCALE, y-3*constants.SCALE
            self.powerObjs.append(rect)
            self.powerObjs.append(mirror_rect)

    def __ocuppiedPosition(self, coord : tuple[int, int]) -> bool: #definir
        if(self.objs):
            pass
    
    def eatPellets(self, remove_point : tuple[int, int]) -> None:
        
        self.__total_pellets -= 1

    def getTotalPellets(self) -> int:
        return self.__total_pellets






g = Game("fraldinha")

while g.itsRunning():
    g.newGame()


