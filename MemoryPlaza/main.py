import pygame, sys, random, os
from pygame.locals import *

#board length = lenght card*8+gap length*7+6
#board height = height card*8+gap height*7+6
#card

FPS = 30
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
CARDWIDTH = 66
CARDHEIGHT = 74
GAP = 10
BOARDWIDTH = 8 * CARDWIDTH + 7 * GAP + 6
BOARDHEIGHT = 8 * CARDHEIGHT + 7 * GAP + 6

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (CARDWIDTH + GAP))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (CARDHEIGHT + GAP))) / 2)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
WHITE = (0, 0, 0)
CYAN = (0, 255, 255)
PURPLE = (128, 0, 128)
PINK = (255, 0, 255)

BGCOLOR = BLACK

MYSTERY = pygame.image.load("Data/Image/mystery.png")
REVEAL = pygame.image.load("Data/Image/reveal.png.png")
JUMPSCARE = pygame.image.load("Data/Image/spuky.png")

UNCOVERED = "uncovered"


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)


def getRandomizedBoard():
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            pass
        board.append(column)
    return board


def leftTopCoordsOfBox(boxx, boxy):
    left = boxx * (CARDWIDTH + GAP) + XMARGIN
    top = boxy * (CARDHEIGHT + GAP) + YMARGIN
    return (left, top)


#def drawCards(boardx, boardy):
#   for i in range(8):
#       for j in range(8):
#           DISPLAYSURF.blit(MYSTERY, (boardx+(CARDWIDTH+GAP)*i, boardy+(CARDHEIGHT+GAP)*j))

def drawBoard(board, revealed):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            DISPLAYSURF.blit(MYSTERY, (left, top))


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, CARDWIDTH, CARDHEIGHT)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def Game():
    pygame.init()
    global FPSCLOCK, DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("In Game")

    mousex = 0
    mousey = 0

    BOARDX = DISPLAYSURF.get_width() / 2 - BOARDWIDTH / 2
    BOARDY = DISPLAYSURF.get_height() / 2 - BOARDHEIGHT / 2

    JUMPSCARESFX = pygame.mixer.Sound("Data/Sound/top_5_scariest_jumpscares.ogg")

    pygame.mixer.music.load("Data/Music/song_game1.mp3")
    pygame.mixer.music.play(-1)

    mainBoard = getRandomBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    while True:

        mouseClicked = False

        DISPLAYSURF.fill(PURPLE)
        BOARD = pygame.draw.rect(DISPLAYSURF, BLACK, ((BOARDX, BOARDY), (BOARDWIDTH, BOARDHEIGHT)), 0)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.mixer.music.stop()
                pygame.display.set_caption("GOODBYE!")
                DISPLAYSURF.blit(JUMPSCARE, (0, 0))
                pygame.display.update()
                JUMPSCARESFX.play()
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            if not revealedBoxes[boxx][boxy]:
                pass
            if not revealedBoxes[boxx][boxy]:
                revealedBoxes[boxx][boxy] = True
                pass
            

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    print("SUP M8SS!!!")
    Game()
