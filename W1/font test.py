import pygame, sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('No fucking way! Text in my window!!!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('fonts/Cafeteria-Bold.otf', 32)
textSurfaceObj = fontObj.render('SUP M8s!!!', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center=(200, 150)

while True:
    window.fill(WHITE)
    window.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()