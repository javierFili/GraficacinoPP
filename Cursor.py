import pygame


class Cursor(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1) #es un rectangulo

    def update(self):
        self.left,self.top=pygame.mouse.get_pos() #mover el rectangulo con el mouse.


