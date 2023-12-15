import abc #Abstract Base Classes
import pygame
from pygame.locals import *
from pygame.surface import Surface
import constants

class GameSprites(abc.ABC):

    @abc.abstractmethod
    def __init__(self, sprite : Surface,vector_of_initial_positions : list[tuple[int, int]], sprite_size : tuple[int, int], scale : float=1.0):
        
        self._to_build_sprite_sheet = sprite
        self._sprite_images_vector = []
            
        sprite_scaled = list(sprite_size)
        sprite_scaled = tuple([scale * coord for coord in sprite_scaled])

        for sprite_pos in vector_of_initial_positions:
                img = self._to_build_sprite_sheet.subsurface(sprite_pos, sprite_size)
                img = pygame.transform.scale(img, sprite_scaled)
                self._sprite_images_vector.append(img)


class Characters(abc.ABC): #abstract class
    
    @abc.abstractmethod
    def __init__(self, spawn_point : list, surface : Surface, speed=10, direction=-1):
        self.__speed = speed #default
        self.__direction = direction #TALVEZ APAGAR
        self.__coordinates = spawn_point
        self.__surface = surface
        self.ref_geometry = None #muito provavel de apagar

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
    def setSpeed(self, value=10):
        self.__speed = value
    
    def getSpeed(self):
        return self.__speed

    def getDirection(self):
        return self.__direction
    
    def setDirection(self, value):
        self.__direction = value
    
    def getPosition(self):
        return self.__coordinates[0], self.__coordinates[1]

class Pacman(pygame.sprite.Sprite, Characters, GameSprites): #definir classe
    def __init__(self, nickname : str, surf: Surface, sprite_sheet : Surface):
        
        self.__has_power = False
        self.__nickname = nickname

        self.__x_pacman = surf.get_width()/2
        self.__y_pacman = surf.get_height()/2 #initial position / TALVEZ APAGAR

        Characters.__init__(self, [self.__x_pacman, self.__y_pacman], surf,  10)

        #****************************REFATORAR************************************
        sprites_initial_points = [(i, j) for i in range(457, 489, 16) for j in range(1, 65, 16)] + [(i, 1) for i in range(489, 681, 16)]

        GameSprites.__init__(self, sprite_sheet, sprites_initial_points, (13, 13), 2)
        pygame.sprite.Sprite.__init__(self)

        self.index_sprites = 0
        self.image = self._sprite_images_vector[self.index_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.__x_pacman, self.__y_pacman

        self.__index_eat = 0
        self.__sprite_vector_eat = [(1, 5, 8, 5), (2, 6, 8, 6), (0, 4, 8, 4), (3, 7, 8, 7)]
        self.__update_sprite_factor = 0

    def update(self): #update method is necessary for pygame.sprite
        if(not self.__update_sprite_factor % (constants.FACTOR_SPEED_SPRITE * self.getSpeed())): #animation depends of speed and clock
            self.__index_sprites = self.eatAnim()
        self.image = self._sprite_images_vector[int(self.__index_sprites)] #image atribute is necessary for pygame.sprite
        self.rect.center = self.getPosition()
        self.__update_sprite_factor += 1

    def eatAnim(self): #animation and effect
        self.__index_eat += 1
        self.__index_eat %= 3
        return self.__sprite_vector_eat[self.getDirection()][int(self.__index_eat)]

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


        Characters.__init__(self, [self.__x_ghost, self.__y_ghost], surf,  10)
        pygame.sprite.Sprite.__init__(self)

        self.__sprite_vector_killer = []
        self.__sprite_vector_prey = []
        self.__sprite_vector_die = []
        self.__ghost_value = ghost_type

        self.setGhostColor(sprite_sheet)
        self.setDirection(1) #teste para o fantasma mexer

    def update(self):
        pass


    def setGhostColor(self, sprite_sheet):
        if(self.__ghost_value == constants.BLINKY): 
            sprites_initial_points = [(i, 65) for i in range(457, 647, 16)] + [(i, 81) for i in range(585, 647)]
        elif(self.__ghost_value == constants.PINKY):
            sprites_initial_points = [(i, 81) for i in range(457, 647, 16)] + [(i, 65) for i in range(585, 647)]
        elif(self.__ghost_value == constants.INKY):
            sprites_initial_points = [(i, 97) for i in range(457, 585, 16)] + [(i, 65) for i in range(585, 647)] + [(i, 81) for i in range(585, 647)]
        elif(self.__ghost_value == constants.CLYDE):
            sprites_initial_points = [(i, 113) for i in range(457, 585, 16)] + [(i, 65) for i in range(585, 647)] + [(i, 81) for i in range(585, 647)]

        GameSprites.__init__(self, sprite_sheet, sprites_initial_points, (14, 14), 2)

    def killerMode():
        pass

    def killerAnim():
        pass
    
    def preyMode():
        pass

    def preyAnim():
        pass

    def dieMode():
        pass

    def dieAnim():
        pass

    def respawn():
        pass

    def behavior(): #AI control for ghosts https://tateviktome-tovmasyan.medium.com/ai-and-pacman-a-story-of-ghosts-intelligence-d2f296c31675
        pass
