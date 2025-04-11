import pygame
from constantes import *
from math import cos, pi

class IoioDee(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = LISTA_IOIO[0]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):
        self.rect.y = self.pos_y + 150*cos(0.5*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 120*cos(1*(pygame.time.get_ticks()-self.t0)/1000)
    

    def piscar(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = LISTA_IOIO[0]
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = LISTA_IOIO[1]

    
    def update(self):
        self.movimentar()
        self.piscar()

class IoioDum(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = pygame.transform.flip(LISTA_IOIO[0], True, False)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):
        self.rect.y = self.pos_y + 150*cos(pi + 0.5*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 120*cos(pi + 1*(pygame.time.get_ticks()-self.t0)/1000)
    

    def piscar(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = pygame.transform.flip(LISTA_IOIO[0], True, False)
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = pygame.transform.flip(LISTA_IOIO[1], True, False)

    
    def update(self):
        self.movimentar()
        self.piscar()