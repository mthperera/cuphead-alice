import pygame
from constantes import *
from math import cos
from random import randint
from Classes.Peca import Peca

class ReiVermelho(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0_pecas = self.t0 = pygame.time.get_ticks()
        self.lancou_pecas = False
        self.image = LISTA_REI[0]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_pecas = pygame.sprite.Group()
    
    def invocar_pecas(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_pecas) % 10000 <= 6500:
            self.image = LISTA_REI[0]
            self.lancou_pecas = False
        elif (self.t1 - self.t0_pecas) % 10000 <= 8000:
            self.image = LISTA_REI[1]
            if not self.lancou_pecas:
                for _ in range(randint(5, 8)):
                    self.grupo_pecas.add(Peca())
                self.lancou_pecas = True
        elif (self.t1 - self.t0_pecas) % 10000 < 10000:
            self.image = LISTA_REI[0]

        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    
    def movimentar(self):
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)
    
    def update(self):
        
        self.invocar_pecas()
        self.movimentar()

