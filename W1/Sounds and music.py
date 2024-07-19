import pygame, sys
from pygame.locals import *
import time


pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Woah sounds and music')

BLACK = (0, 0 ,0)

soundObj = pygame.mixer.Sound('sounds/s9465.ogg')


pygame.mixer.music.load('music/61504_newgrounds_paper_.mp3')
pygame.mixer.music.play(-1, 0, 0)

while True:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            soundObj.play()
            time.sleep(6)
            pygame.quit()
            sys.exit()
    pygame.display.update()