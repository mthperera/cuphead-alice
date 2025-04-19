import pygame
from constantes import *
from math import cos

class PlataformaRainha(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = IMAGEM_PLATAFORMA_RAINHA
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidade_y = 120
        self.pos_x = LARGURA_TELA - 256
        self.pos_y = 200
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
    

    def movimentar(self):

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)


    def update(self):
        
        self.movimentar()

        self.mask = pygame.mask.from_surface(self.image)