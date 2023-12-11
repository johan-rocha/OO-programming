import abc #Abstract Base Classes
import pygame
from pygame.locals import *
from pygame.surface import Surface
from time import sleep

class GameSprites(abc.ABC):

    @abc.abstractmethod
    def __init__(self, sprite : Surface,vector_of_initial_positions : list[tuple[int, int]],
                  sprite_size : tuple[int, int], scale : int=1):
        
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
    def __init__(self, init_coord : list, surface : Surface, speed=10, color=(0, 0, 0), direction=-1):
        self.__speed = speed #default
        self.__color = color
        self.__direction = direction #TALVEZ APAGAR
        self.__coordinates = init_coord
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

class Pacman(pygame.sprite.Sprite, Characters, GameSprites): #definir classe
    def __init__(self, nickname : str, surf: Surface, sprite_sheet : Surface):
        self.__x_pacman = surf.get_width()/2
        self.__y_pacman = surf.get_height()/2 #initial position / TALVEZ APAGAR

        Characters.__init__(self, [self.__x_pacman, self.__y_pacman], surf,  10, (244, 206, 14))

        self.__has_power = False
        self.__nickname = nickname

        #****************************REFATORAR************************************
        GameSprites.__init__(self, sprite_sheet, 
                             [(i, j) for i in range(457, 489, 16) for j in range(1, 65, 16)] + [(i, 1) for i in range(489, 681, 16)],
                             (13, 13), 3
            )
        
        pygame.sprite.Sprite.__init__(self)

        self.index_sprites = 0
        self.image = self._sprite_images_vector[self.index_sprites]
        self.rect = self.image.get_rect()
        self.rect.center = self.__x_pacman, self.__y_pacman
        print(f"width = {self.rect.width} height = {self.rect.height} center = {self.rect.center}")


    def update(self): #update method is necessary for pygame.sprite
        self.index_sprites %= 19
        self.index_sprites += 0.5
        self.image = self._sprite_images_vector[int(self.index_sprites)] #image atribute is necessary for pygame.sprite

    def eat(self):
        return 

    def die():
        pass

    def incrementPelletsEaten():
        pass

    def defineHasPower():
        pass

class Ghost(Characters, GameSprites, pygame.sprite.Sprite): #definir classe
    def __init__(self, color : tuple, surf: Surface, sprite_sheet : Surface):
        self.__x_ghost = surf.get_width()/2
        self.__y_ghost = surf.get_width()/2


        Characters.__init__(self, [self.__x_ghost, self.__y_ghost], surf, 10, color)

        pygame.sprite.Sprite.__init__(self) 

        self.__ghost_value = 0
        self.setDirection(1)

    def respawn():
        pass

    def arrayList():
        pass

    def behavior():
        pass
