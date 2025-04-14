import pygame
from constantes import *
from random import choice, randint

class Peca(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = randint(230, LARGURA_TELA - 230)
        self.pos_y = randint(-400, -50)
        self.velocidade_y = 200
        self.t0 = pygame.time.get_ticks()
        self.image = choice(LISTA_PECAS)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Movimento de queda simples, por meio de movimento retilíneo uniforme.
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1

    
    def update(self):

        self.movimentar()
        
        # Checando limites do mapa:
        if self.rect.y > ALTURA_TELA:
            self.kill()
        elif self.rect.x < 0 or self.rect.x > LARGURA_TELA:
            self.kill()