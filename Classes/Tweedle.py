import pygame
from constantes import *
from math import cos
from Classes.Ovo import Ovo

class TweedleDee(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0_ovo = self.t0 = pygame.time.get_ticks()
        self.lancou_ovo = False
        self.image = LISTA_TEEDLE_OVO[0]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_ovos = pygame.sprite.Group()
    
    def jogar_ovo(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_ovo) % 3000 <= 600:
            self.image = LISTA_TEEDLE_OVO[0]
            self.lancou_ovo = False
        elif (self.t1 - self.t0_ovo) % 3000 <= 1200:
            self.image = LISTA_TEEDLE_OVO[1]
        elif (self.t1 - self.t0_ovo) % 3000 <= 1800:
            self.image = LISTA_TEEDLE_OVO[2]
        elif (self.t1 - self.t0_ovo) % 3000 <= 2400:
            self.image = LISTA_TEEDLE_OVO[3]
            if not self.lancou_ovo:
                self.grupo_ovos.add(Ovo(155, 65, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                self.lancou_ovo = True
        elif (self.t1 - self.t0_ovo) % 3000 < 3000:
            self.image = LISTA_TEEDLE_OVO[2]
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    
    def movimentar(self):
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self):
        
        self.jogar_ovo()
        self.movimentar()

class TweedleDum(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0_ovo = self.t0 = pygame.time.get_ticks()
        self.lancou_ovo = False
        self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[0], True, False)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_ovos = pygame.sprite.Group()
    
    def jogar_ovo(self):
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_ovo) % 3000 <= 600:
            self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[0], True, False)
            self.lancou_ovo = False
        elif (self.t1 - self.t0_ovo) % 3000 <= 1200:
            self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[1], True, False)
        elif (self.t1 - self.t0_ovo) % 3000 <= 1800:
            self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[2], True, False)
        elif (self.t1 - self.t0_ovo) % 3000 <= 2400:
            self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[3], True, False)
            if not self.lancou_ovo:
                self.grupo_ovos.add(Ovo(LARGURA_TELA-155, 65, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                self.lancou_ovo = True
        elif (self.t1 - self.t0_ovo) % 3000 < 3000:
            self.image = pygame.transform.flip(LISTA_TEEDLE_OVO[2], True, False)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    
    def movimentar(self):
        self.rect.y = self.pos_y + 10*cos(2*(pygame.time.get_ticks()-self.t0)/1000)
    
    def update(self):
        
        self.jogar_ovo()
        self.movimentar()