import pygame

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Drawing Rectangles")
pos_x = 300
pos_y = 250
vel_x = 2
vel_y = 1

class Paint:
    def __init__(self):
        self.str = ""

    def DrawFrame(self):
        color = 255, 255, 0
        width = 0
        pos = pos_x, pos_y, 100, 100
        pygame.draw.rect(screen, color, pos, width)
        pygame.display.update(
        

def main():
    paint = Paint()
    paint.DrawFrame()

main()

