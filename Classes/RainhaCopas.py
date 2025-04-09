from constantes import *
import pygame

class RainhaCopas():

    def __init__(self):
        self.image = None
        self.pos_x = LARGURA_TELA - 100
        self.pos_y = ALTURA_TELA - 100
    
    def invocar_coracoes(self):
        pass

    def invocar_cartinhas(self):
        pass

    def animar_morte(self):
        pass
    
    def desenhar(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))