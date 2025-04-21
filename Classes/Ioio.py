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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Ioio fazendo uma Figura de Lissajous por meio de dois MHS ortogonais.
        # Isso foi feito para dar uma sensação de movimento mais aleatório.
        self.rect.y = self.pos_y + 200*cos(1*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 150*cos(1.5*(pygame.time.get_ticks()-self.t0)/1000)
    

    def piscar(self):

        # Animação do Ioio piscando:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = LISTA_IOIO[0]
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = LISTA_IOIO[1]

    
    def update(self):

        self.movimentar()
        self.piscar()

        self.mask = pygame.mask.from_surface(self.image)


class IoioDum(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0 = pygame.time.get_ticks()
        self.image = pygame.transform.flip(LISTA_IOIO[0], True, False)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
    
    
    def movimentar(self):

        # Ioio fazendo uma Figura de Lissajous por meio de dois MHS ortogonais.
        # Isso foi feito para dar uma sensação de movimento mais aleatório.
        self.rect.y = self.pos_y + 200*cos(pi + 2*(pygame.time.get_ticks()-self.t0)/1000)
        self.rect.x = self.pos_x + 150*cos(pi + 2.5*(pygame.time.get_ticks()-self.t0)/1000)
    

    def piscar(self):

        # Animação do Ioio piscando:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0) % 2000 <= 1500:
            self.image = pygame.transform.flip(LISTA_IOIO[0], True, False)
        elif (self.t1 - self.t0) % 2000 <= 2000:
            self.image = pygame.transform.flip(LISTA_IOIO[1], True, False)

    
    def update(self):
        
        self.movimentar()
        self.piscar()

        self.mask = pygame.mask.from_surface(self.image)