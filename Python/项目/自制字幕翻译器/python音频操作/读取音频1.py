#法一
# import os
# os.system('D://test/1.mp3')
#法二
import pygame
pygame.init()
track = pygame.mixer.music.load('D://test/1.mp3')
pygame.mixer.music.play()
time.sleep()
pygame.mixer.music.stop()
#法三
