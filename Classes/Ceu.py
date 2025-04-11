import pygame
from constantes import *

class Ceu():
    def __init__(self):
        self.pos_x = 0
        self.velocidade_y = 120
        self.t0 = pygame.time.get_ticks()
        self.image = IMAGEM_FUNDO_DRAGAO
    
    def movimentar(self):
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.rect.y += self.velocidade_y * self.dt

        self.t0 = self.t1
    

class Ceu_01(Ceu, pygame.sprite.Sprite):
    def __init__(self):
        Ceu.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        # pygame.sprite.Sprite().__init__(self) -> Pq não?

        self.pos_y = 0
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def update(self):

        self.movimentar()

        if self.rect.y >= LARGURA_TELA:
            self.rect.y = -self.image.get_width()
        

class Ceu_02(Ceu, pygame.sprite.Sprite):
    def __init__(self):
        Ceu.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.pos_y = -self.image.get_width()
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def update(self):

        self.movimentar()

        if self.rect.y >= LARGURA_TELA:
            self.rect.y = 0