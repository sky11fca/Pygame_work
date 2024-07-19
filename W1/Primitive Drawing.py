import sys

import pygame
from pygame.locals import *

pygame.init()

# setting up the window

window = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing Preetttty Pictures!!!')

# some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# BEGIN DRAWING

window.fill(WHITE)

pygame.draw.polygon(window, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
# it goes something like this
# the screen object, the color, coordinates: (X, Y, W, H), (X, Y) for start or end, width -> thickness of the line
pygame.draw.line(window, BLUE, (60, 60), (120, 60), 4) # for drawing lines, width means the thickness of the line
pygame.draw.line(window, BLUE, (120, 60), (60, 120))
pygame.draw.line(window, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(window, BLUE, (300, 50), 20, 0) # without mentioning width or width=0 means filling the object with respective color
pygame.draw.ellipse(window, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(window, RED, (200, 150, 100, 50))

# Drawing individual pixels
pixObj = pygame.PixelArray(window)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()