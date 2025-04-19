import pygame
from constantes import *
from math import cos
from Classes.Livro import Livro

class RainhaVermelha(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = x
        self.pos_y = y
        self.t0_livro = self.t0 = pygame.time.get_ticks()
        self.lancou_livro = False
        self.image = LISTA_RAINHA_VERMELHA[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.grupo_livros = pygame.sprite.Group()
        self.vidas = 20
    
    
    def jogar_livro(self):

        # Realizando aremesso de livos a cada certo período em ms:
        self.t1 = pygame.time.get_ticks()

        if (self.t1 - self.t0_livro) % 3200 <= 800:
            self.image = LISTA_RAINHA_VERMELHA[2]
            self.lancou_livro = False
        elif (self.t1 - self.t0_livro) % 3200 <= 1600:
            self.image = LISTA_RAINHA_VERMELHA[1]
        elif (self.t1 - self.t0_livro) % 3200 <= 2400:
            self.image = LISTA_RAINHA_VERMELHA[2]
        elif (self.t1 - self.t0_livro) % 3200 < 3200:
            self.image = LISTA_RAINHA_VERMELHA[4]
            if not self.lancou_livro:
                self.grupo_livros.add(Livro(LARGURA_TELA - 200, 105, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                self.lancou_livro = True
        
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        
    
    def movimentar(self):

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 5 * cos((pygame.time.get_ticks() - self.t0)/1000)
    
    
    def update(self):
        
        self.jogar_livro()
        self.movimentar()

        if self.vidas <= 0:
            self.kill()
        
        self.mask = pygame.mask.from_surface(self.image)

