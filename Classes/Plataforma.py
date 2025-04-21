import pygame
from constantes import *

class Plataforma(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = PLATAFORMA_PEDRA
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidade_y = 80
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
        
        self.mask = pygame.mask.from_surface(self.image)


class PlataformaEstavel(pygame.sprite.Sprite):

    def __init__(self, x):
        super().__init__()
        self.image = PLATAFORMA_PEDRA_ESTAVEL
        self.image.fill((255, 255, 255, 255), special_flags=pygame.BLEND_RGBA_MULT)
        self.pos_x = x
        self.pos_y = ALTURA_TELA
        self.rect = self.image.get_rect(midbottom=(self.pos_x, self.pos_y))
        self.mask = pygame.mask.from_surface(self.image)
        self.t0 = pygame.time.get_ticks()


    def update(self):

        self.mask = pygame.mask.from_surface(self.image)