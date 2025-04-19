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
        self.image = pygame.transform.flip(LISTA_REI[0], True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_pecas = pygame.sprite.Group()
        self.vidas = 20
    

    def invocar_pecas(self):

        # Invocando peças do céu a cada certo tempo em ms:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_pecas) % 10000 <= 6500:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[0], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)
            self.lancou_pecas = False
        elif (self.t1 - self.t0_pecas) % 10000 <= 8000:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[1], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)
            if not self.lancou_pecas:
                for _ in range(randint(5, 8)):
                    self.grupo_pecas.add(Peca())
                self.lancou_pecas = True
        elif (self.t1 - self.t0_pecas) % 10000 < 10000:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(LISTA_REI[0], True, False)
            self.rect = self.image.get_rect(center = antigo_centro)

        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    
    def movimentar(self):

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)
    
    
    def update(self):
        
        self.invocar_pecas()
        self.movimentar()

        if self.vidas <= 0:
            self.kill()

        self.mask = pygame.mask.from_surface(self.image)

