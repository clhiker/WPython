import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT)%2==0, 'even number is necessary'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH*(BOXSIZE+GAPSIZE)))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT*(BOXSIZE+GAPSIZE)))/2)

#divide the colors
#           RED   G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BGCOLOR        = NAVYBLUE
LIGHTBGCOLOR   = GRAY
BOXCOLOR       = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT   = 'donut'
SQUARE  = 'square'
DIAMOND = 'diamond'
LINES   = 'lines'
OVAL    = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS)*(ALLSHAPES)*2 >= BOARDWIDTH * BOARDHEIGHT,
"Board is too big for the number of shapes/colors defined."






























