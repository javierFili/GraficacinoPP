import pygame
import math
from pygame.locals import *
# dimensiones de la ventana
# WIDTH, HEIGHT = 700, 600
# thickness = segment = space = 1

class Bresenham:

    def update(self):
        pygame.display.update()
        # pygame.time.delay(50)

    def pintar(self, x, y, pa_, color_):
        if x >= 0 and y >= 0 and x <= 1000 and y <= 600:
            pa_[int(x)][int(y)] = color_


    def algoritmoSegmentado(self, x0, y0, x1, y1, color_, sprite_, segmento, espacio, grosor):
        dx = x1 - x0
        dy = y1 - y0
        contador = 0
        llenar = False
        stepx = stepy = 1
        if dx < 0:
            dx = -dx
            stepx = -1
        else:
            stepx = 1

        if dy < 0:
            dy = -dy
            stepy = -1
        else:
            stepy = 1
        x = x0
        y = y0
        pa_ = pygame.PixelArray(sprite_)
        if dx > dy:
            p = 2 * dy - dx
            incE = 2 * dy
            incNE = 2 * (dy - dx)

            while x != x1:
                x = x + stepx
                if p < 0:
                    p = p + incE
                else:
                    y = y + stepy
                    p = p + incNE
                if espacio != 0:
                    if llenar:
                        if contador < segmento:
                            pa_[int(x)][int(y)] = color_
                            arriba = True
                            sumaAlGrosor = 1
                            for i in range(grosor):
                                if arriba:
                                    arriba = False
                                    self.pintar(x, y + sumaAlGrosor, pa_, color_)
                                else:
                                    arriba = True
                                    self.pintar(x, y - sumaAlGrosor, pa_, color_)
                                    sumaAlGrosor = sumaAlGrosor + 1
                            contador = contador + 1
                        else:
                            self.update()
                            if espacio > 1:
                                llenar = False
                                contador = 1
                            else:
                                contador = 0
                    else:
                        if contador < espacio:
                            contador = contador + 1
                        else:
                            contador = 0
                            llenar = True
                else:
                    pa_[int(x)][int(y)] = color_
                    arriba = True
                    sumaAlGrosor = 1
                    for i in range(grosor):
                        if arriba:
                            arriba = False
                            self.pintar(x, y + sumaAlGrosor, pa_, color_)
                        else:
                            arriba = True
                            self.pintar(x, y - sumaAlGrosor, pa_, color_)
                            sumaAlGrosor = sumaAlGrosor + 1
                    contador = contador + 1
                    if contador == segmento:
                        contador = 0
                        self.update()

        else:
            p = 2 * dx - dy
            incE = 2 * dx
            incNE = 2 * (dx - dy)

            while y != y1:
                y = y + stepy
                if p < 0:
                    p = p + incE
                else:
                    x = x + stepx
                    p = p + incNE
                if espacio != 0:
                    if llenar:
                        if contador < segmento:
                            pa_[int(x)][int(y)] = color_
                            derecha = True
                            sumaAlGrosor = 1
                            for i in range(grosor):
                                if derecha:
                                    derecha = False
                                    self.pintar(x + sumaAlGrosor, y, pa_, color_)
                                else:
                                    derecha = True
                                    self.pintar(x - sumaAlGrosor, y, pa_, color_)
                                    sumaAlGrosor = sumaAlGrosor + 1
                            contador = contador + 1
                        else:
                            self.update()
                            if espacio > 1:
                                llenar = False
                                contador = 1
                            else:
                                contador = 0
                    else:
                        if contador < espacio:
                            contador = contador + 1
                        else:
                            contador = 0
                            llenar = True
                else:
                    pa_[int(x)][int(y)] = color_
                    derecha = True
                    sumaAlGrosor = 1
                    for i in range(grosor):
                        if derecha:
                            derecha = False
                            self.pintar(x + sumaAlGrosor, y, pa_, color_)
                        else:
                            derecha = True
                            self.pintar(x - sumaAlGrosor, y, pa_, color_)
                            sumaAlGrosor = sumaAlGrosor + 1
                    contador = contador + 1
                    if contador == segmento:
                        contador = 0
                        self.update()
        self.update()


    # def __init__(self, segmento, espacio, grosor):
    #     x0 = 0
    #     y0 = 0
    #     textoVacio = "Presionar"
    #     textoPunto = "Última coordenada:"
    #     pygame.init()
    #     pygame.display.set_caption(textoVacio)
    #     screen = pygame.display.set_mode((WIDTH, HEIGHT))
    #     WHITE = (255, 255, 255)
    #     screen.fill(WHITE)
    #     BLACK = (0, 0, 0)
    #     pygame.display.update()
    #     # pygame.time.delay(2000)
    #     # algoritmoSegmentado(x0, y0, x1, y1, BLACK, screen, segmento, espacio, grosor)
    #     comp = True
    #     contadorClicks = 0
    #     while comp:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 comp = False
    #             else:
    #                 if event.type == pygame.MOUSEBUTTONDOWN:
    #                     pr = pygame.mouse.get_pos()
    #                     prx = pr[0]
    #                     pry = pr[1]
    #                     if contadorClicks == 2:
    #                         contadorClicks = 0
    #                         pygame.display.set_caption(textoVacio)
    #                     else:
    #                         pygame.display.set_caption(textoPunto + str(prx) + '-' + str(pry))
    #                         if contadorClicks == 0:
    #                             x0 = prx
    #                             y0 = pry
    #                             pygame.display.update()
    #                         else:
    #                             self.algoritmoSegmentado(x0, y0, prx, pry, BLACK, screen, segmento, espacio, grosor)
    #                         contadorClicks += 1
    #
    #     pygame.quit()
    def __init__(self):
        pass
