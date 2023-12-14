import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint
from Characters import *

main_dir = os.path.dirname(__file__)
images_dir = os.path.join(main_dir, "images")
#sound_dir = os.path.dirname(main_dir, "sounds")

pygame.init()
pygame.font.init()
width = 452
height = 516

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("FGA-PACMAN")

clock = pygame.time.Clock()


x_obstaculo = randint(40, 600)
y_obstaculo = randint(50, 430)

score = 0
fonte = pygame.font.SysFont('liberationmono', 30, True, False) #config text
#verify fonts: pygame.font.get_fonts()

sprite_sheet = pygame.image.load(os.path.join(images_dir, 'pacman_sprite.png')).convert_alpha()



pacman = Pacman("cleitin", screen, sprite_sheet)
#purple_ghost = Ghost((113, 29, 176), screen, sprite_sheet)

all_sprites = pygame.sprite.Group()
all_sprites.add(pacman)

while True:
    
    clock.tick(20) #taxa de atualização
    screen.fill((0, 0, 0)) #tela preenchida pela cor preta, atualizar tela
    mensagem = f'Score: {score}' #message score text
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #score text


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                pacman.setDirection(0)
            if event.key == K_w:        
                pacman.setDirection(1)
            if event.key == K_d:
                pacman.setDirection(2)
            if event.key == K_s:
                pacman.setDirection(3)


    pacman.move()
    #purple_ghost.move()
    all_sprites.draw(screen)
    all_sprites.update()


    screen.blit(texto_formatado, (450, 20)) #text
    pygame.display.update()
 

"""     obstaculo = pygame.draw.rect(screen, (255,0,0), (x_obstaculo,y_obstaculo,40,50))

    if(obstaculo.colliderect(pacman.ref_geometry)):
        x_obstaculo = randint(40, 600)
        y_obstaculo = randint(50, 430)
        score+=1
    """



"""     purple_ghost.ref_geometry = pygame.draw.circle(screen, purple_ghost.getColor(), purple_ghost.getPosition(), 15)

    pacman.ref_geometry = pygame.draw.circle(screen, pacman.getColor(), pacman.getPosition(), 12)"""


