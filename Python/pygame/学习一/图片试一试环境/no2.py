mouse_image_filename = 'flower.jpg'
import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode ((640, 480), 0, 32)
pygame.display.set_caption("shift")
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
while True :
  for event in pygame.event.get ():
    if event.type ==QUIT:
      exit()

  x, y = pygame.mouse.get_pos()
  x-= mouse_cursor.get_width() / 2
  y-= mouse_cursor.get_height() / 2
  screen.blit(mouse_cursor, (x, y))
  pygame.display.update()
