import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF =pygame.display.set_mode((400,300))

soundObj = pygame.mixer.Sound("1.wav")
soundObj.play()

import time
time.sleep (1)
soundObj.stop()

while True : 
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
