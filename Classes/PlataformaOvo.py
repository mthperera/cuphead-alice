import pygame
from constantes import *
from math import cos

class PlataformaOvoDee(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = IMAGEM_CASCA_OVO
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    
    def update(self):

        self.movimentar()


class PlataformaOvoDum(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = pygame.transform.flip(IMAGEM_CASCA_OVO, True, False)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    
    def update(self):
        
        self.movimentar()

