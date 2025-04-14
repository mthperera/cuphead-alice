import pygame
from constantes import *
from random import choice
from math import sqrt

class Ovo(pygame.sprite.Sprite):

    def __init__(self, x, y, x_alvo, y_alvo):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.dx = x_alvo - self.pos_x
        self.dy = y_alvo - self.pos_y
        self.velocidade_x = self.dx/sqrt(self.dx**2 + self.dy**2) * 350
        self.velocidade_y = self.dy/sqrt(self.dx**2 + self.dy**2) * 350
        self.t0 = pygame.time.get_ticks()
        self.image = choice(LISTA_OVOS)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Esse movimento inicia em direção ao personagem, já que forçamos o vetor velocidade 
        # ser radial em coordenadas polares.
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.x += self.velocidade_x * self.dt
        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1

    
    def update(self):
        
        self.movimentar()
        
        # Chencando limites do mapa:
        if self.rect.y > ALTURA_TELA or self.rect.y < 0:
            self.kill()
        elif self.rect.x < 0 or self.rect.x > LARGURA_TELA:
            self.kill()