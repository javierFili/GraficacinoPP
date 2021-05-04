import pygame
from pygame.locals import *

"""los que estab en la linea (64,66,7476) y con son lo que arregle del anterior codigo que pase

"""
global vista
class AlgoritmoModificadoDDA:


    def __init__(self, grosor, segmentacion):
        pygame.init()
        self.vista = pygame.display.set_mode((1000, 500))
        self.clock = pygame.time.Clock()
        self.inicializador(grosor, segmentacion,self.vista)

    def inicializador(self,grosor,segmentacion,vista):
        xa=0
        ya=0
        xb=0
        yb=0
        conta = 0
        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pr = pygame.mouse.get_pos()
                        prx = str(pr[0])
                        pry = str(pr[1])
                        titul = prx + "-" + pry
                        pygame.display.set_caption(titul)
                        pos=pygame.mouse.get_pos()
                        if conta==0:
                            xa= int (pos[0])
                            ya= int (pos[1])
                            conta+=1
                        else:
                            if conta==1:
                                xb = int(pos[0])
                                yb = int(pos[1])
                                #print(xa,ya,self.xb,self.yb)
                                self.algoritmoEnLineaDDA(xa, ya, xb, yb,grosor, segmentacion,vista)
                                conta+=1
                                pygame.display.update()
                            else:
                               conta=0

        pygame.quit()

    def algoritmoEnLineaDDA (self, xa, ya, xb, yb, grosor, segmentacion,vista):
        sprite_ = vista
        color_ = pygame.Color(255, 200, 200)

        if grosor > 1 and segmentacion > 1:
            self.ddaEnsaSegmen(xa, ya, xb, yb, segmentacion, grosor, color_, sprite_)
        else:
            if segmentacion > 1:
                self.ddaSegmentada(xa, ya, xb, yb, segmentacion, color_, sprite_);
            else:
                if grosor > 1:
                    self.ddaEnsanchada(xa, ya, xb, yb, grosor, color_, sprite_)
                else:
                    if grosor == 1 and segmentacion == 1:
                        self.normalDDA(xa, ya, xb, yb, color_,sprite_)
                    else:
                        pass
                    'sacar mensaje de error.'

    def ddaSegmentada (self,xa, ya, xb, yb, segmentacion, color_, sprite_):

        dx = xb - xa
        dy = yb - ya
        x = xa
        y = ya
        seg=segmentacion
        if (dx == 0):
            pa_ = pygame.PixelArray(sprite_)
            pa_[int(x)][int(y)] = pygame.Color(255, 255, 0)
            pa_[int(x)][int(y)] = color_
            for k in range(1, int((abs(dy)))):
                if seg!=0:
                    seg=seg-1
                    y = y + dy / (abs(dy))
                else:
                    y = y + dy / (abs(dy))
                    pa_[int(x)][int(y)] = color_
                    seg = segmentacion
        else:
            if (abs(dx) > abs(dy)):
                numPasos = abs(dx)
            else:
                numPasos = abs(dy)

            xIncremen = dx / numPasos
            yIncremen = dy / numPasos

            pa_ = pygame.PixelArray(sprite_)
            pa_[int(x)][int(y)] = pygame.Color(255, 255, 0)
            for k in range(1, int(numPasos)):
                if seg!=0:
                    seg=seg-1
                    x = x + xIncremen
                    y = y + yIncremen
                else:
                    x = x + xIncremen
                    y = y + yIncremen
                    pa_[int(x)][int(y)] = color_
                    seg = segmentacion

        del pa_

    def ddaEnsanchada (self,xa, ya, xb, yb, ancho, color_, sprite_):
        self.normalDDA(xa, ya, xb, yb, color_, sprite_)
        ancho = ancho - 1
        control = False
        xa1 = xa
        xa2 = xa
        ya1 = ya
        ya2 = ya
        xb1 = xb
        xb2 = xb
        yb1 = yb
        yb2 = yb
        while ancho >= 0:
            if control:
                ya1 = ya1+1
                yb1 = yb1+1
                self.normalDDA(xa1, ya1, xb1, yb1, color_, sprite_)
                control = False
                ancho = ancho - 1
                pygame.display.update()
            else:
                xa2 = xa2-1
                xb2 = xb2-1
                self.normalDDA(xa2, ya2, xb2, yb2, color_, sprite_)
                control = True
                ancho = ancho - 1
                pygame.display.update()

    def ddaEnsaSegmen(self,xa, ya, xb, yb, segmentacion, ancho, color_, sprite_):
        self.ddaSegmentada(xa, ya, xb, yb, segmentacion, color_, sprite_)
        ancho = ancho - 1
        control = False
        xa1 = xa
        xa2 = xa
        ya1 = ya
        ya2 = ya
        xb1 = xb
        xb2 = xb
        yb1 = yb
        yb2 = yb
        while ancho >= 0:
            if control:
                ya1 = ya1 + 1
                yb1 = yb1 + 1
                self.ddaSegmentada(xa1, ya1, xb1, yb1, segmentacion, color_, sprite_)
                control = False
                ancho = ancho - 1
            else:
                xa2 = xa2 - 1
                xb2 = xb2 - 1
                self.ddaSegmentada(xa2, ya2, xb2, yb2, segmentacion, color_, sprite_)
                control = True
                ancho =ancho - 1

    def normalDDA (self,xa, ya, xb, yb, color_, sprite_):
        dx = xb - xa
        dy = yb - ya
        x = xa
        y = ya
        if (dx == 0):
            numPasos = (abs(dy))
            yIncremen = dy / numPasos
            pa_ = pygame.PixelArray(sprite_)
            pa_[int(x)][int(y)] = pygame.Color(255, 255, 0)
            for k in range(1, int(numPasos)):
                y = y + yIncremen
                pa_[int(x)][int(y)] = color_
        else:
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
                pa_[int(x)][int(y)] = color_
            del pa_

#puebas
if __name__=='__main__' :
    al=AlgoritmoModificadoDDA(3,4)
