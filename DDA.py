import pygame
import time
from pygame.locals import *

global vista


def algortmoEnLineaDDA(xa, ya, xb, yb, color_, sprite_):
    dx = xb - xa
    dy = yb - ya
    x = xa
    y = ya

    if (dx==0):
      numPasos=(abs(dy))
      yIncremen=dy/numPasos

      pa_=pygame.PixelArray(sprite_)
      pa_[int(x)][int(y)]=pygame.Color(255,255,0)

      for k in range(1,int(numPasos)):
        y=y+yIncremen
        pygame.display.update()
        time.sleep(0.1)
        pa_[int(x)][int(y)]=color_
    else :
        if (abs(dx) > abs(dy)):
            numPasos = abs(dx)
        else:
            numPasos = abs(dy)

        xIncremen = dx / numPasos
        yIncremen = dy / numPasos

        pa_ = pygame.PixelArray(sprite_)
        pa_[int(x)][int(y)] = pygame.Color(255, 255, 0)
        for k in range(1, int(numPasos)):
            x = x + xIncremen
            y = y + yIncremen
            pygame.display.update()
            time.sleep(0.1)
            pa_[int(x)][int(y)] = color_
    del pa_

def run():
    x0 = int(input("x0:"))
    y0 = int(input("y0:"))
    x1 = int(input("x1:"))
    y1 = int(input("y1:"))
    pygame.init()
    vista = pygame.display.set_mode((700, 600), 0, 32)
    #algortmoEnLineaDDA(50, 30, 500, 30, pygame.Color(255, 200, 200), screen)
    #algortmoEnLineaDDA(300,300,300,80,pygame.Color(255,200,200),screen)
    #algortmoEnLineaDDA(300, 300, 100, 100, pygame.Color(255,200,200), vista)
    algortmoEnLineaDDA(x0, y0, x1, y1, pygame.Color(255, 200, 200), vista)
    while 1:
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()

if __name__ == '__main__':
    run()