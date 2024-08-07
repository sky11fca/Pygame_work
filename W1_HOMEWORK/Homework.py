import pygame, sys
from pygame.locals import *
import time

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 240

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('HELL!')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 0, 255)

ShQIMG = pygame.image.load('img/Shadow_Queen.png')
ShQX = 0
ShQY = 0
direct = 'left'

fontObj = pygame.font.Font('fonts/Cafeteria-Bold.otf', 64)
textObj = fontObj.render("Please end my suffering!!!", 1, WHITE)
textRect = textObj.get_rect()
textRect.center = (WIDTH/2, HEIGHT/2)

soundObj = pygame.mixer.Sound('sounds/s9465.ogg')
pygame.mixer.music.load('music/61504_newgrounds_paper_.mp3')
pygame.mixer.music.play(-1, 0, 0)

while True:
    WIN.fill(PURPLE)
    pygame.draw.rect(WIN, PINK, (100, 100, 1080, 520))

    if direct == 'left':
        ShQX += 1
        if ShQX == 1112:
            direct = 'down'
    elif direct == 'down':
        ShQY += 1
        if ShQY == 474:
            direct = 'right'
    elif direct == 'right':
        ShQX -= 1
        if ShQX == 0:
            direct = 'up'
    elif direct == 'up':
        ShQY -= 1
        if ShQY == 0:
            direct = 'left'

    WIN.blit(ShQIMG, (ShQX, ShQY))
    WIN.blit(textObj, textRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.display.set_caption("MOTHERFUCKER WHY DID YOU LEAVE")
            pygame.mixer.music.stop()
            soundObj.play()
            pygame.draw.rect(WIN, (0, 0, 0, 255), (0, 0, 1280, 720))
            pygame.display.update()
            time.sleep(6)
            pygame.display.set_caption("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
