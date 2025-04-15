import pygame
from constantes import *
from math import sqrt

class Bolinho(pygame.sprite.Sprite):

    def __init__(self, x, y, alvo_x, alvo_y):
        pygame.sprite.Sprite.__init__(self, x, y, alvo_x, alvo_y)
        self.delta_x = alvo_x - x
        self.delta_y = alvo_y - y
        self.image = BOLINHO
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.velocidade = 150
        self.velocidade_x = self.delta_x / sqrt(self.delta_x**2 + self.delta_y**2) * self.velocidade
        self.velocidade_y = self.delta_y / sqrt(self.delta_x**2 + self.delta_y**2) * self.velocidade
        self.t0 = pygame.time.get_ticks()


    def movimentar(self):
        
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1


    def update(self):
        
        if (pygame.time.get_ticks() - self.t0) > 500:
            self.movimentar()
