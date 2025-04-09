from constantes import *
from math import cos
import pygame

class RainhaCopas():

    def __init__(self):
        self.image = LISTA_INVOCAR_CORACAO[2]
        self.t0_movimento = pygame.time.get_ticks()
        self.pos_x_inicial = LARGURA_TELA - 200
        self.pos_x = self.pos_x_inicial
        self.pos_y_inicial = ALTURA_TELA - 239
        self.pos_y = self.pos_y_inicial
        self.ataque_coracao = "Sem ataque"
        self.t0_ataque = 0
        self.vida = 50
        self.dano = 1
    
    def invocar_coracoes(self):

        if (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 250:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 500:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 750:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 1000:
            self.image = LISTA_INVOCAR_CORACAO[3]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 1250:
            self.image = LISTA_INVOCAR_CORACAO[4]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 1500:
            self.image = LISTA_INVOCAR_CORACAO[5]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 1750:
            self.image = LISTA_INVOCAR_CORACAO[6]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 2000:
            self.image = LISTA_INVOCAR_CORACAO[5]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 2250:
            self.image = LISTA_INVOCAR_CORACAO[4]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 2500:
            self.image = LISTA_INVOCAR_CORACAO[3]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 2750:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 3000:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  3500 <= 3250:
            self.image = LISTA_INVOCAR_CORACAO[2] 
        else:
            self.vivo = "Sem ataque"
            self.image = LISTA_INVOCAR_CORACAO[2]
    
    def movimentar(self):
        # Figura de Lissajous:
        self.pos_x = self.pos_x_inicial + 50*cos(1*(pygame.time.get_ticks()-self.t0_movimento)/1000)
        self.pos_y = self.pos_y_inicial + 3*cos(2*(pygame.time.get_ticks()-self.t0_movimento)/1000)

    def animar_morte(self):
        pass
    
    def desenhar(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))