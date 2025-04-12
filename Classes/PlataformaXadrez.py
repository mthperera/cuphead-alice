import pygame
from constantes import *
from math import cos

class PlataformaXadrez(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = IMAGEM_PLATAFORMA_XADREZ   
        self.velocidade_y = 120
        self.pos_x = (LARGURA_TELA - self.image.get_width())//2
        self.pos_y = (ALTURA_TELA - self.image.get_height())//2 + 145
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
    

    def movimentar(self):
        self.rect.y = self.pos_y + 10 * cos((pygame.time.get_ticks() - self.t0)/1000)


    def update(self):
        self.movimentar()