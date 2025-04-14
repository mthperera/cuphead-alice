import pygame
from constantes import *
from random import randint

class Coracao(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.t0 = pygame.time.get_ticks()
        self.t0_morte = 0
        self.image = IMAGEM_CORACAO
        self.pos_x = randint(50, LARGURA_TELA - 200)
        self.pos_y = randint(-800, -500)
        self.velocidade_y = 200
        self.vivo = "Vivo"
        self.vidas = 1
        self.dano = 1
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))


    def movimentar(self):

        # Movimentação retilínea simples:
        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        self.rect.y += self.velocidade_y * self.delta_t

        self.t0 = self.t1
    

    def animar_morte(self):

        # Animando a morte, de modo a dar um efeito de coração quebrando:
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


    def update(self):
            
        if self.vivo == "Vivo":
            self.movimentar()
        if self.rect.y > ALTURA_TELA - 48 and self.vivo == "Vivo":
            self.t0_morte = pygame.time.get_ticks()
            self.vivo = "Morrendo"
        if self.vivo == "Morrendo":
            self.animar_morte()
        if self.vivo == "Morto":
            self.kill()