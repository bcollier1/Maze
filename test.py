import pygame, time, sys
from shapes import Triangle, Rectangle, Oval
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width = 1080
height = 720

#pygame.Surface((width, height))

DISPLAYSURF = pygame.display.set_mode((width,height))
pygame.display.set_caption('Maze Game')
background = pygame.image.load('maze.png')

while True:

    DISPLAYSURF.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mouse_x,mouse_y = pygame.mouse.get_pos()
    #pygame.Surface.get_at(mouse_x, mouse_y)
    print(tuple(DISPLAYSURF.get_at((mouse_x, mouse_y))))
    #print(mouse_x, mouse_y)

    pygame.display.update()
    fpsClock.tick(FPS)