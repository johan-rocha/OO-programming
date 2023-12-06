import Game, Characters, pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480

x_pos = 0
y_pos = 0


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FGA-PACMAN")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(screen, (244, 206, 14), (x_pos, y_pos), 5)

    pygame.display.update()