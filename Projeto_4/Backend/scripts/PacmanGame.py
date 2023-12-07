import pygame
from pygame.locals import *
from sys import exit
from random import randint
from Game import *
from Characters import *

pygame.init()
pygame.font.init()

width = 640
height = 480

x_obstaculo = randint(40, 600)
y_obstaculo = randint(50, 430)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FGA-PACMAN")
clock = pygame.time.Clock()

score = 0
fonte = pygame.font.SysFont('liberationmono', 30, True, False) #config text
#verify fonts: pygame.font.get_fonts()

pacman = Pacman(screen)

while True:
    
    clock.tick(8) #taxa de atualização
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
        """
        if pygame.key.get_pressed()[K_a]:
            x_pos -= 20
        if pygame.key.get_pressed()[K_w]:
            y_pos -= 20
        if pygame.key.get_pressed()[K_d]:
            x_pos += 20
        if pygame.key.get_pressed()[K_s]:
            y_pos += 20
        """
    pacman.move()
    pacman.pacman_ref_geometry = pygame.draw.circle(screen, pacman.getColor(), pacman.getPosition(), 12)
    obstaculo = pygame.draw.rect(screen, (255,0,0), (x_obstaculo,y_obstaculo,40,50))

    if(obstaculo.colliderect(pacman.pacman_ref_geometry)):
        x_obstaculo = randint(40, 600)
        y_obstaculo = randint(50, 430)
        score+=1
    screen.blit(texto_formatado, (450, 20)) #text
    pygame.display.update()

