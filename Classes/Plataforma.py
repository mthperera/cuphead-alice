import pygame
from constantes import *

class Plataforma(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = PLATAFORMA_PEDRA
        self.velocidade_y = 120
        self.pos_x = x
        self.pos_y = y
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
    

    def movimentar(self):

        # Plataforma em movimento simples de queda sem aceleração:
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1


    def update(self):

        self.movimentar()

        # Checando limites do mapa:
        if self.rect.y > ALTURA_TELA:
            self.kill()