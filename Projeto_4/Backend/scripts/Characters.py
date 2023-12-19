import abc #Abstract Base Classes
import time
import numpy as np
import pygame
from pygame.locals import *
from pygame.surface import Surface
import constants


class Timer():
    def __init__(self) -> None:
        self.__timer_on = False
        self.__initial_time = 0
        self.__time_traveled = 0 #diferenca de tempo atual e passado
        self.__timer_set = 0


    def initTimer(self, range_in_seconds):
        if(self.__timer_on):
            pass
        else:
            self.__initial_time = time.perf_counter()
            self.__timer_on = True
            self.__timer_set = range_in_seconds
   
    def timer(self):
        if(self.__timer_on):
            if(self.__time_traveled >= self.__timer_set):
                    self.__timer_on = False
            self.__time_traveled = time.perf_counter() - self.__initial_time
            return self.__time_traveled
    
    def getTimeLeft(self):
        return self.__timer_set - self.__time_traveled

    def timeout(self):
        return (not self.__timer_on)
    
    #fazer cronometro tambem para o Game









class GameSprites(abc.ABC):

    @abc.abstractmethod
    def __init__(self, sprite : Surface,vector_of_initial_positions : list[tuple[int, int]], sprite_size : tuple[int, int], scale : float=1.0):
        
        self.__to_build_sprite_sheet = sprite
        self._sprite_images_vector = []
            
        sprite_scaled = list(sprite_size)
        sprite_scaled = tuple([scale * coord for coord in sprite_scaled])

        for sprite_pos in vector_of_initial_positions:
                img = self.__to_build_sprite_sheet.subsurface(sprite_pos, sprite_size)
                img.set_colorkey(constants.BLACK)
                img.convert_alpha()
                img = pygame.transform.scale(img, sprite_scaled)
                self._sprite_images_vector.append(img)









class Characters(abc.ABC): #abstract class
    
    @abc.abstractmethod
    def __init__(self, spawn_point : list, surface : Surface, speed=constants.DEFAULT_SPEED, direction=-1):
        self.__speed = speed #default
        self.__direction = direction
        self.__next_direction = direction
        self._collided = False
        self.__coordinates = spawn_point
        self.__surface = surface
        self.ref_geometry = None #muito provavel de apagar

    def move(self) -> None:
        if(self.__direction == -1):
            pass
        elif(self.__direction == constants.LEFT):
            self.__coordinates[0] -= self.__speed
        elif(self.__direction == constants.UP):
            self.__coordinates[1] -= self.__speed
        elif(self.__direction == constants.RIGHT):
            self.__coordinates[0] += self.__speed
        elif(self.__direction == constants.DOWN):
            self.__coordinates[1] += self.__speed

        if(self.__coordinates[0] >= self.__surface.get_width()-1): #teleport character
            self.__coordinates[0] = 1
        elif(self.__coordinates[0] <= 1): #teleport character
            self.__coordinates[0] = self.__surface.get_width()-1

    #ver como funciona, usando como exemplo
    def setSpeed(self, speed=constants.DEFAULT_SPEED):
        self.__speed = speed
    
    def getSpeed(self):
        return self.__speed

    def getDirection(self):
        return self.__direction
    
    def setDirection(self, value): #seta a proxima direcao a ser seguida
        self.__next_direction = value
    
    def _verifyDirection(self, left, up, right, down, center):
    #testa os sentidos e sua colisoes para ver a borda para teste de colisao adequada
        
        temp_a, temp_b = right #pygame rect midtop offset
        temp_a -= 1
        right = (temp_a, temp_b)
        temp_a, temp_b = down
        temp_b -= 1
        down = (temp_a, temp_b)

        if(not self._collided):
            if(self.__direction == -1):
                pass
            elif(self.__direction == constants.LEFT):
                if(self.checkColision(left)):
                    self.__direction = -1
                    self._collided = True
            elif(self.__direction == constants.UP):
                if(self.checkColision(up)):
                    self.__direction = -1
                    self._collided = True
            elif(self.__direction == constants.RIGHT):
                if(self.checkColision(right)):
                    self.__direction = -1
                    self._collided = True
            elif(self.__direction == constants.DOWN):
                if(self.checkColision(down)):
                    self.__direction = -1
                    self._collided = True

        if(self.__next_direction == -1):
            pass
        elif(self.__next_direction == constants.LEFT):
            if(self.checkColision(left)):
                pass
            else:
                self.__direction = self.__next_direction
                self._collided = False
        elif(self.__next_direction == constants.UP):
            if(self.checkColision(up)):
                pass
            else:
                self.__direction = self.__next_direction
                self._collided = False
        elif(self.__next_direction == constants.RIGHT):
            if(self.checkColision(right)):
                pass
            else:
                self.__direction = self.__next_direction
                self._collided = False
        elif(self.__next_direction == constants.DOWN):
            if(self.checkColision(down)):
                pass
            else:
                self.__direction = self.__next_direction
                self._collided = False
    #se colidir
        #se esta no sentido que ja estava, para (setDiretion -1)
        #senao, não faz nada
    #se nao colidiu -> self.__direction = self.__next_direction
    
    def getPosition(self):
        return self.__coordinates[0], self.__coordinates[1]
    
    def checkColision(self, obj_position : tuple[int, int]): #model pygame -> (column, row)
        col, row = int(obj_position[0]), (obj_position[1])
        position = int(row * constants.WIDTH*constants.SCALE + col)
        byte_offset = int(position * np.dtype(int).itemsize)

        with open("map.bin", 'rb') as file:
            file.seek(byte_offset)
            estado_colisao = np.fromfile(file, dtype=int, count=1)
        return estado_colisao.item()
    







class Pacman(pygame.sprite.Sprite, Characters, GameSprites): #definir classe
    def __init__(self, nickname : str, surf: Surface, sprite_sheet : Surface):
        
        self.__x_pacman = 112*constants.SCALE
        self.__y_pacman = 139*constants.SCALE #initial position / TALVEZ APAGAR

        Characters.__init__(self, [self.__x_pacman, self.__y_pacman], surf,  constants.DEFAULT_SPEED)

        #****************************REFATORAR************************************
        sprites_initial_points = [(i, j) for i in range(457, 489, 16) for j in range(1, 65, 16)] + [(i, 1) for i in range(489, 681, 16)]

        GameSprites.__init__(self, sprite_sheet, sprites_initial_points, (13, 13), constants.SCALE)
        pygame.sprite.Sprite.__init__(self)

        self.__has_power = False
        self.__nickname = nickname
        self.__sprite_vector_eat = [(1, 5, 8, 5), (2, 6, 8, 6), (0, 4, 8, 4), (3, 7, 8, 7)]

        self.__index_sprites = 0
        self.__index_eat_anim = 0
        self.__update_sprite_factor = 0

        self.image = self._sprite_images_vector[self.__index_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.__x_pacman, self.__y_pacman
        self.b_box_colision = pygame.Rect(0,0,3,3)
        self.b_box_colision.center = self.rect.center

    def update(self): #update method is necessary for pygame.sprite
        if(not self.__update_sprite_factor % round(constants.FACTOR_SPEED_SPRITE_PACMAN * self.getSpeed())): #animation depends of speed and clock
            self.__update_sprite_factor = 0
            if(not self._collided):
                self.__index_sprites = self.eatAnim()

        self.image = self._sprite_images_vector[self.__index_sprites] #image atribute is necessary for pygame.sprite #tirei o int do self.__index_sprites
        self.rect.center = self.getPosition()
        self.b_box_colision.center = self.rect.center
        self._verifyDirection(self.b_box_colision.midleft, self.b_box_colision.midtop, self.b_box_colision.midright, self.b_box_colision.midbottom, self.b_box_colision.center)
        self.__update_sprite_factor += 1

    def eatAnim(self): #animation and effect
        self.__index_eat_anim += 1
        self.__index_eat_anim %= 3
        return self.__sprite_vector_eat[self.getDirection()][int(self.__index_eat_anim)]

    def dieAnim(): #print(self.rect.width)
        pass

    def incrementPelletsEaten():
        pass

    def defineHasPower():
        pass















class Ghost(pygame.sprite.Sprite, Characters, GameSprites): #definir classe

    def __init__(self, ghost_type : int, surf: Surface, sprite_sheet : Surface):
        pass
        self.__x_ghost = surf.get_width()/2
        self.__y_ghost = surf.get_width()/2


        Characters.__init__(self, [self.__x_ghost, self.__y_ghost], surf,  constants.DEFAULT_SPEED)
        pygame.sprite.Sprite.__init__(self)

        self.__timer = Timer()
        self.__ghost_value = ghost_type
        self.__ghost_state = constants.ALIVE 
        self.__sprite_vector_killer_anim = [(2, 3), (4, 5), (0, 1), (6, 7)]
        self.__sprite_vector_prey_anim = [(8, 9), (8, 11, 10, 9)] #prey/prey finish
        self.__sprite_vector_die_anim = [13, 14, 12, 15]#left, up, right, down

        self.setGhostColor(sprite_sheet)
        self.setDirection(constants.LEFT) #teste para o fantasma mexer

        self.__update_sprite_factor = 0
        self.__index_sprites = 0
        self.__index_move_anim = 0
        self.__index_prey_finish_anim = 0

        self.image = self._sprite_images_vector[self.__index_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.__x_ghost, self.__y_ghost
        self.b_box_colision = pygame.Rect(0,0,3,3)
        self.b_box_colision.center = self.rect.center

    def update(self):
        if(not self.__update_sprite_factor % round(constants.FACTOR_SPEED_SPRITE_GHOST * self.getSpeed())):
            self.__update_sprite_factor = 0
            self.__index_move_anim += 1 #killer and prey
            self.__index_move_anim %= 2
            if(self.__ghost_state == constants.ALIVE):
                self.killerMode()
                self.__index_sprites = self.killerAnim()

            elif(self.__ghost_state == constants.PREY):
                self.preyMode()
                self.__index_sprites = self.preyAnim()

            elif(self.__ghost_state == constants.DIE):
                self.dieMode()
                self.__index_sprites = self.dieAnim()
        
        self.image = self._sprite_images_vector[self.__index_sprites]
        self.rect.center = self.getPosition()
        self.b_box_colision.center = self.rect.center
        self._verifyDirection(self.b_box_colision.midleft, self.b_box_colision.midtop, self.b_box_colision.midright, self.b_box_colision.midbottom, self.b_box_colision.center)
        self.__update_sprite_factor += 1
        self.behavior()


    def setGhostColor(self, sprite_sheet):
        if(self.__ghost_value == constants.BLINKY): 
            sprites_initial_points = [(i, 65) for i in range(457, 647, 16)] + [(i, 81) for i in range(585, 647, 16)]
        elif(self.__ghost_value == constants.PINKY): #dando errado
            sprites_initial_points = [(i, 81) for i in range(457, 585, 16)] + [(i, 65) for i in range(585, 647, 16)] + [(i, 81) for i in range(585, 647, 16)]
        elif(self.__ghost_value == constants.INKY):
            sprites_initial_points = [(i, 97) for i in range(457, 585, 16)] + [(i, 65) for i in range(585, 647, 16)] + [(i, 81) for i in range(585, 647, 16)]
        elif(self.__ghost_value == constants.CLYDE):
            sprites_initial_points = [(i, 113) for i in range(457, 585, 16)] + [(i, 65) for i in range(585, 647, 16)] + [(i, 81) for i in range(585, 647, 16)]

        GameSprites.__init__(self, sprite_sheet, sprites_initial_points, (14, 14), constants.SCALE)

    def killerMode(self):
        self.__ghost_state = constants.ALIVE

    def killerAnim(self):
        return self.__sprite_vector_killer_anim[self.getDirection()][self.__index_move_anim]
    
    def preyMode(self):
        self.__ghost_state = constants.PREY
        self.setSpeed(constants.DEFAULT_SPEED/2)
        self.__timer.initTimer(10)
        self.__timer.timer()
        if(self.__timer.timeout()): ##definir o tempo em timer(x)
            self.__ghost_state = constants.ALIVE
            self.setSpeed(constants.DEFAULT_SPEED)


    def preyAnim(self):
        if(self.__timer.getTimeLeft() > 3):
            return self.__sprite_vector_prey_anim[0][self.__index_move_anim]
        #senao se o tempo estiver acabando
        else:
            return self.preyAnimFinishTimer()

        
    
    def preyAnimFinishTimer(self): #arrumar finish timer
        self.__index_prey_finish_anim += 1
        self.__index_prey_finish_anim %= 4
        return self.__sprite_vector_prey_anim[1][self.__index_prey_finish_anim]

    def dieMode(self):
        self.__ghost_state = constants.DIE

    def dieAnim(self):
        return self.__sprite_vector_die_anim[self.getDirection()]

    def respawn(self):
        pass

    def behavior(self): #AI control for ghosts https://tateviktome-tovmasyan.medium.com/ai-and-pacman-a-story-of-ghosts-intelligence-d2f296c31675
        pass
