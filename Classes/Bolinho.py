import pygame
from constantes import *
from math import cos, sin, radians

class Bolinho(pygame.sprite.Sprite):

    def __init__(self, x, y, angulo):
        pygame.sprite.Sprite.__init__(self)
        self.image = BOLINHO
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (x, y))
        self.velocidade = 500
        self.velocidade_x = self.velocidade * cos(radians(angulo))
        self.velocidade_y = - self.velocidade * sin(radians(angulo))
        self.t0 = pygame.time.get_ticks()


    def movimentar(self):
        
        now = pygame.time.get_ticks()
        self.dt = (now - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = now


    def update(self):
        
        self.movimentar()
        
        if self.rect.x > LARGURA_TELA or self.rect.x < 0:
            self.kill()
        elif self.rect.y > ALTURA_TELA or self.rect.y < 0:
            self.kill()

        self.mask = pygame.mask.from_surface(self.image)