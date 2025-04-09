import pygame
from constantes import *
from math import sqrt, atan, degrees

class Cartinha():
    
    def __init__(self):
        self.t0 = pygame.time.get_ticks()
        self.imagens = LISTA_IMAGENS_CARTINHA
        self.image = LISTA_IMAGENS_CARTINHA[0]
        self.masks = MASKS_CARTINHA
        self.movimento = None
        self.pos_x = 0
        self.pos_y = 0
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.velocidade = 70
        self.aceleracao = 60
        self.vivo = "Vivo"
        self.t0_morte = 0
        self.vidas = 1
        self.dano = 1


    def movimentar_acelerando(self, alvo_x, alvo_y):
        self.delta_x = alvo_x - self.pos_x
        self.delta_y = alvo_y - self.pos_y

        try:
            self.aceleracao_x = ((self.delta_x)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao
            self.aceleracao_y = ((self.delta_y)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao
        except:
            self.aceleracao_x = 0
            self.aceleracao_y = 0
        
        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        if 20 < self.pos_x < LARGURA_TELA - 64:
            self.pos_x += self.velocidade_x * self.delta_t
            self.velocidade_x += self.aceleracao_x * self.delta_t
        elif self.pos_x <= 20:
            self.pos_x = 21
            self.velocidade_x = 0
        elif self.pos_x >= LARGURA_TELA - 64:
            self.pos_x = LARGURA_TELA - 65
            self.velocidade_x = 0

        if 10 < self.pos_y < ALTURA_TELA - 64:
            self.pos_y += self.velocidade_y * self.delta_t
            self.velocidade_y += self.aceleracao_y * self.delta_t
        elif self.pos_y <= 10:
            self.pos_y = 11
            self.velocidade_y = 0
        elif self.pos_y >= ALTURA_TELA - 64:
            self.pos_y = ALTURA_TELA - 65
            self.velocidade_y = 0

        self.t0 = self.t1


    def movimentar_perseguindo(self, alvo_x, alvo_y):
        self.delta_x = alvo_x - self.pos_x
        self.delta_y = alvo_y - self.pos_y

        try:
            self.velocidade_x = ((self.delta_x)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.velocidade
            self.velocidade_y = ((self.delta_y)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.velocidade
        except:
            self.velocidade_x = 0
            self.velocidade_y = 0
        
        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        if 20 < self.pos_x < LARGURA_TELA - 64:
            self.pos_x += self.velocidade_x * self.delta_t
        elif self.pos_x <= 20:
            self.pos_x = 21
            self.velocidade_x = 0
        elif self.pos_x >= LARGURA_TELA - 64:
            self.pos_x = LARGURA_TELA - 65
            self.velocidade_x = 0

        if 10 < self.pos_y < ALTURA_TELA - 64:
            self.pos_y += self.velocidade_y * self.delta_t
        elif self.pos_y <= 10:
            self.pos_y = 11
            self.velocidade_y = 0
        elif self.pos_y >= ALTURA_TELA - 64:
            self.pos_y = ALTURA_TELA - 65
            self.velocidade_y = 0

        self.t0 = self.t1

    def animar(self):

        if pygame.time.get_ticks() % 500 >= 250:
            self.image = LISTA_IMAGENS_CARTINHA[0]
            self.mask = MASKS_CARTINHA[0]
        else:
            self.image = LISTA_IMAGENS_CARTINHA[1]
            self.mask = MASKS_CARTINHA[1]
    
    def rotacionar(self):
        self.angulo = degrees(-atan(self.velocidade_x/self.velocidade))
        self.image = pygame.transform.rotate(self.image, self.angulo)
    
    def animar_morte(self):
        
        if (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 400:
            self.image = LISTA_EXPLOSAO_CARTINHA[0]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 800:
            self.image = LISTA_EXPLOSAO_CARTINHA[1]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 1200:
            self.image = LISTA_EXPLOSAO_CARTINHA[2]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 1600:
            self.image = LISTA_EXPLOSAO_CARTINHA[3]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 2000:
            self.image = LISTA_EXPLOSAO_CARTINHA[4]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 2400:
            self.image = LISTA_EXPLOSAO_CARTINHA[5]
            self.image = pygame.transform.rotate(self.image, self.angulo)
        else:
            self.vivo = "Morto"
    

    def desenhar(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))