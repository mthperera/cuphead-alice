import pygame
from constantes import *
from math import cos

class TweedleDee(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0_ovo = self.t0 = pygame.time.get_ticks()
        self.ovo_lancar = False
        self.ovo_lancado = False
        self.image = LISTA_TEEDLE_OVO[0]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def jogar_ovo(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_ovo) % 3000 <= 600:
            self.image = LISTA_TEEDLE_OVO[0]
        elif (self.t1 - self.t0_ovo) % 3000 <= 1200:
            self.image = LISTA_TEEDLE_OVO[1]
        elif (self.t1 - self.t0_ovo) % 3000 <= 1800:
            self.image = LISTA_TEEDLE_OVO[2]
            if not self.ovo_lancado:
                self.ovo_lancar = True
        elif (self.t1 - self.t0_ovo) % 3000 <= 2400:
            self.image = LISTA_TEEDLE_OVO[3]

        elif (self.t1 - self.t0_ovo) % 3000 < 3000:
            self.image = LISTA_TEEDLE_OVO[2]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    def movimentar(self):
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self):
        
        self.jogar_ovo()
        self.movimentar()