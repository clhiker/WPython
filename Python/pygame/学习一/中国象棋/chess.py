import pygame ,sys
from pygame.locals import *
pygame.init()
chess = 'chess.jpg'
screen = pygame.display.set_mode ((464,517), 0, 32)
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(chess).convert()


while True :
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  screen.blit(background, (0,0))
  pygame.display.update()
