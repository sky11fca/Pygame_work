import pygame, sys
from pygame.locals import *

pygame.init()

# Setting the fps
FPS = 30
fpsClock = pygame.time.Clock()

# setting the window
window = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("I honestly don't know")

WHITE = (255, 255, 255)

# Creates a random png of Shadow Queen I saved on to SSD for some reason plus coordinates
ShQIMG = pygame.image.load('img/Shadow_Queen.png')
ShQX = 10
ShQY = 10
direction = 'right'

while True:
    window.fill(WHITE)

    if direction == 'right':
        ShQX += 5
        if ShQX == 280:
            direction = 'down'
    elif direction == 'down':
        ShQY += 5
        if ShQY == 220:
            direction = 'left'
    elif direction == 'left':
        ShQX -= 5
        if ShQX == 10:
            direction = 'up'
    elif direction == 'up':
        ShQY -= 5
        if ShQY == 10:
            direction = 'right'

    window.blit(ShQIMG, (ShQX, ShQY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

# HW! Fix the code such that the random image of Shadow Queen will walk in circles at a resolution of 1280x720p
# Upload what you have done on Github
