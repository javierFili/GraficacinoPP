import pygame
import math
from Bresenham import Bresenham

from pygame.locals import *
class Figuras:

    # def __init__(self):
    #     pass

    def update(self):
        pygame.display.update()
        pygame.time.delay(50)


    def pintar(self, x, y, pa_, color_):
        if x >= 0 and y >= 0 and x <= 1000 and y <= 600:
            pa_[int(x)][int(y)] = color_


    def dibujarlinea(self, x0, y0, x1, y1, sprite_, color_, segmento, espacio, grosor):
        bres = Bresenham()
        bres.algoritmoSegmentado(x0, y0, x1, y1, color_, sprite_, segmento, espacio, grosor)

    def cuadrilatero(self, listaP, screen, color, segmento, espacio, grosor):
        pxIzq, pyIzq = listaP[0]
        pxDer, pyDer = listaP[3]
        self.dibujarlinea(pxIzq, pyIzq, pxDer, pyIzq, screen, color, segmento, espacio, grosor)
        self.dibujarlinea(pxIzq, pyIzq, pxIzq, pyDer, screen, color, segmento, espacio, grosor)
        self.dibujarlinea(pxIzq, pyDer, pxDer, pyDer, screen, color, segmento, espacio, grosor)
        self.dibujarlinea(pxDer, pyDer, pxDer, pyIzq, screen, color, segmento, espacio, grosor)


    def triangulo(self,listaP, screen, color,segmento,espacio,grosor):
        pxA, pyA = listaP[0]
        pxB, pyB = listaP[1]
        pxC, pyC = listaP[2]
        self.dibujarlinea(pxA, pyA, pxB, pyB, screen, color,segmento,espacio,grosor)
        self.dibujarlinea(pxA, pyA, pxC, pyC, screen, color,segmento,espacio,grosor)
        self.dibujarlinea(pxB, pyB, pxC, pyC, screen, color,segmento,espacio,grosor)

    def circulo(self, listaP, color, sprite_):
        theta = math.radians(0)
        centrox, centroy = listaP[0]
        radio = listaP[1][0]
        x = radio
        y = 0
        pa_ = pygame.PixelArray(sprite_)
        while theta <= 2*math.pi:
            self.pintar(x+centrox,y+centroy, pa_, color)
            self.pintar(x + centrox + 1, y + centroy, pa_, color)
            self.pintar(x + centrox - 1, y + centroy, pa_, color)
            self.pintar(x + centrox, y + centroy + 1, pa_, color)
            self.pintar(x + centrox, y + centroy - 1, pa_, color)
            theta += math.radians(1)
            xd = radio*math.cos(theta)
            x = math.floor(xd)
            yd = radio * math.sin(theta)
            y = math.floor(yd)

