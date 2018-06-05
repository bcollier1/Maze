import pygame, sys
from pygame.locals import *
from random import *
from tkinter import *

pygame.init()

def start():

    FPS = 60
    fpsClock = pygame.time.Clock()
    score = 0
    counter = 0

    DISPLAYSURF = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Maze Game')
    level1 = pygame.image.load('maze.png')
    level2 = pygame.image.load('maze2.png')
    level3 = pygame.image.load('maze3.png')
    myfont = pygame.font.SysFont("monospace", 16)
    clevel = 1

    UP = 'up'
    LEFT = 'left'
    RIGHT = 'right'
    DOWN = 'down'

    sprite = pygame.image.load('marble.png')
    sprite2 = pygame.image.load('marble2.png')
    dot = pygame.image.load('dot.png')
    dot_x = (randrange(0, 1080))
    dot_y = (randrange(0, 720))
    spritex = 7
    spritey = 520

    while True:
        if counter % 1 == 0:
            score += 1

        if clevel == 1:
            level = DISPLAYSURF.blit(level1, (0, 0))
            DISPLAYSURF.blit(sprite, (spritex, spritey,))

        elif clevel == 2:
            level = DISPLAYSURF.blit(level2, (0, 0))
            DISPLAYSURF.blit(sprite2, (spritex, spritey))

        elif clevel == 3:
            level = DISPLAYSURF.blit(level3, (0,0))
            DISPLAYSURF.blit(sprite2, (spritex, spritey))

        #if (tuple(DISPLAYSURF.get_at((dot_x, dot_y))) == (255, 255, 255, 255) or tuple(DISPLAYSURF.get_at(((dot_x + 17), (dot_y + 17)))) == (255, 255, 255,255) or
                #tuple(DISPLAYSURF.get_at(((dot_x + 17), dot_y))) == (255, 255, 255, 255) or tuple(DISPLAYSURF.get_at((dot_x, (dot_y + 17)))) == (255, 255, 255, 255)):
            #DISPLAYSURF.blit(dot, (dot_x, dot_y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    sprite

                elif event.key == K_RIGHT:
                    sprite

                elif event.key == K_UP:
                    sprite

                elif event.key == K_DOWN:
                    sprite

                elif event.key == K_t:
                    sprite

                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            spritex -= 2

        elif keys_pressed[K_RIGHT]:
            spritex += 2

        elif keys_pressed[K_UP] and (spritey-5) > 0:
            spritey -= 2

        elif keys_pressed[K_DOWN]:
            spritey += 2

        elif keys_pressed[K_t]:
            spritex = 950
            spritey = 20

        if clevel == 1:
            if tuple(DISPLAYSURF.get_at((spritex, spritey))) == (0, 0, 0, 255) or tuple(DISPLAYSURF.get_at(((spritex + 30), (spritey + 30)))) == (0, 0, 0, 255):
                spritex = 7
                spritey = 520
        #if clevel == 2:
            #if tuple(DISPLAYSURF.get_at((spritex, spritey))) == (0, 0, 0, 255) or tuple(DISPLAYSURF.get_at(((spritex + 19), (spritey + 20)))) == (0, 0, 0, 255):
                #spritex = 505
                #spritey = 4

        if clevel == 3:
            if tuple(DISPLAYSURF.get_at((spritex, spritey))) == (0, 0, 0, 255) or tuple(DISPLAYSURF.get_at(((spritex + 30), (spritey + 30)))) == (0, 0, 0, 255):
                spritex = 550
                spritey = 10

        if clevel == 1:
            if tuple(DISPLAYSURF.get_at((spritex, spritey))) == (255, 8, 0, 255) or tuple(DISPLAYSURF.get_at(((spritex + 32), (spritey + 33)))) == (255, 8, 0, 255):
                clevel = 2
                sprite = sprite2
                spritex = 505
                spritey = 4

        if clevel == 2:
            if tuple(DISPLAYSURF.get_at((spritex, spritey))) == (255, 8, 0, 255): #or tuple(DISPLAYSURF.get_at(((spritex + 33), (spritey + 33)))) == (255, 8, 0, 255):
                clevel = 3
                spritex = 550
                spritey = 10


        scoretext = myfont.render("Score {0}".format(score), 1, (0, 0, 0))
        DISPLAYSURF.blit(scoretext, (20, 10))

        pygame.display.update()
        fpsClock.tick(FPS)

def close():
    exit()

window = Tk()

b1 = Button(window, text = "Start", command = start)
b1.pack()
b2 = Button(window, text = "Close", command = close)
b2.pack()

window.mainloop()