import pygame, sys, random, os
from pygame.locals import *
def Game():
    
    pygame.init()
    global FPSCLOCK, DISPLAYSURF
    FPS = 30
    WINDOWWIDTH = 1280
    WINDOWHEIGHT = 720

    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)
    WHITE = (0, 0, 0)
    CYAN = (0, 255, 255)
    PURPLE = (128, 0, 128)
    PINK = (255, 0, 255)

    BGCOLOR = BLACK

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("In Game")

    pygame.mixer.music.load("~/PycharmProjects/MemoryPlaza/Data/Music/song_game.mp3")
    pygame.mixer.music.play(-1)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)
