import pygame,sys
from pygame.locals import *

pygame.init()
# set up the window
DISPLAYSURF = pygame.display .set_mode((400,300))
pygame.display .set_caption ('hello world')

#color
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)

fj = pygame.font.Font('freesanbold.ttf', 32)
tsj = fj.render('hello world',True, GREEN,BLUE)
trj = tsj.get_rect()
trj.center = (200,150)

while True:
  DISPLAYSURF.fill(WHITE)
  DISPLAYSURF.blit(tsj,trj)
  for event in pygame.event .get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display .update ()
