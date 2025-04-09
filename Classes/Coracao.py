import pygame
from constantes import *

class Coracao():
    
    def __init__(self):
        self.t0 = pygame.time.get_ticks()
        self.t0_morte = 0
        self.image = IMAGEM_CORACAO
        self.masks = MASK_CORACAO
        self.pos_x = 0
        self.pos_y = 0
        self.velocidade_y = 200
        self.vivo = "Vivo"
        self.vidas = 1
        self.dano = 1


    def movimentar(self):
        
        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        self.pos_y += self.velocidade_y * self.delta_t

        self.t0 = self.t1
    

    def animar_morte(self):

        if (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 250:
            self.image = LISTA_EXPLOSAO_CORACAO[0]
        elif (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 500:
            self.image = LISTA_EXPLOSAO_CORACAO[1]
        elif (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 750:
            self.image = LISTA_EXPLOSAO_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 1000:
            self.image = LISTA_EXPLOSAO_CORACAO[3]
        elif (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 1250:
            self.image = LISTA_EXPLOSAO_CORACAO[4]
        elif (pygame.time.get_ticks() - self.t0_morte) %  1750 <= 1500:
            self.image = LISTA_EXPLOSAO_CORACAO[5]
        else:
            self.vivo = "Morto"


    def desenhar(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))