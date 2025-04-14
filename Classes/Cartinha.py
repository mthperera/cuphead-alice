import pygame
from constantes import *
from math import sqrt, atan, degrees
from random import randint

class Cartinha(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.t0 = pygame.time.get_ticks()
        self.imagem = LISTA_IMAGENS_CARTINHA[0]
        self.image = LISTA_IMAGENS_CARTINHA[0]
        self.masks = MASKS_CARTINHA
        self.pos_x = LARGURA_TELA - 200 + randint(-150, 50)
        self.pos_y = ALTURA_TELA + randint(-300, -150)
        self.velocidade_x = randint(-80, -10)
        self.velocidade_y = randint(-50, -10)
        self.aceleracao = 50
        self.angulo = 0
        self.vivo = "Vivo"
        self.t0_morte = 0
        self.vidas = 1
        self.dano = 1
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.delta_t_acel = 5000


    def movimentar_acelerando(self, alvo_x, alvo_y):

        # Movimentação das cartinhas seguindo um alvo -> Curva de Perseguição (modelo matemático).
        # Além disso, evita que elas saiam do mapa.

        self.alvo_x = alvo_x
        self.alvo_y = alvo_y

        self.delta_x = self.alvo_x - self.rect.centerx
        self.delta_y = self.alvo_y - self.rect.centery

        try:
            self.aceleracao_x = ((self.delta_x)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao 
            self.aceleracao_y = ((self.delta_y)/sqrt(self.delta_x**2 + self.delta_y**2)) * self.aceleracao
        except:
            self.aceleracao_x = 0
            self.aceleracao_y = 0

        self.t1 = pygame.time.get_ticks()
        self.delta_t = (self.t1 - self.t0)/1000

        self.velocidade_x += self.aceleracao_x * self.delta_t * 1.5
        self.velocidade_y += self.aceleracao_y * self.delta_t * 1.5

        if 20 < self.rect.x < LARGURA_TELA - 64:
            self.rect.x += self.velocidade_x * self.delta_t
        elif self.rect.x <= 20:
            self.rect.x = 21
            self.velocidade_x = 0
        elif self.rect.x >= LARGURA_TELA - 64:
            self.rect.x = LARGURA_TELA - 65
            self.velocidade_x = 0

        if 10 < self.rect.y < ALTURA_TELA - 115:
            self.rect.y += self.velocidade_y * self.delta_t
        elif self.rect.y <= 10:
            self.rect.y = 11
            self.velocidade_y = 0
        elif self.rect.y >= ALTURA_TELA - 115:
            self.rect.y = ALTURA_TELA - 116
            self.velocidade_y = 0

        self.t0 = self.t1


    def animar(self):

        # Animando o bater das asas das cartinhas:
        if pygame.time.get_ticks() % 500 >= 250:
            self.imagem = LISTA_IMAGENS_CARTINHA[0]
            self.mask = MASKS_CARTINHA[0]
        else:
            self.imagem = LISTA_IMAGENS_CARTINHA[1]
            self.mask = MASKS_CARTINHA[1]
    

    def rotacionar(self):

        # Rotacionando a cartinha, a fim de parecer que ela se move em direção ao jogador:
        self.delta_x = self.alvo_x - self.rect.centerx
        self.delta_y = self.alvo_y - self.rect.centery

        try:
            theta = degrees(atan(abs(self.velocidade_y/self.velocidade_x)))
            if self.velocidade_y < 0:
                if self.velocidade_x < 0:
                    self.angulo = 90 - theta
                else:
                    self.angulo = theta - 90
            else:
                if self.velocidade_x < 0:
                    self.angulo = 90 + theta
                else:
                    self.angulo = - theta - 90
        except:
            self.angulo = 0
        
        self.image = pygame.transform.rotate(self.imagem, self.angulo)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
    

    def animar_morte(self):
        
        # Realizando a animação da morte de uma cartinha:
        if (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 400:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[0]
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 800:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[1]
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 1200:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[2]
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 1600:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[3]
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 2000:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[4]
        elif (pygame.time.get_ticks() - self.t0_morte) %  2800 <= 2400:
            self.imagem = LISTA_EXPLOSAO_CARTINHA[5] 
        else:
            self.vivo = "Morto"
        
        centro = self.rect.center
        self.image = pygame.transform.rotate(self.imagem, self.angulo)
        self.rect = self.image.get_rect(center=centro)
    

    def update(self):

        if self.vivo == "Vivo":
            self.animar()
        elif self.vivo == "Morrendo":
            self.animar_morte()
        elif self.vivo == "Morto":
            self.kill()

        self.rotacionar()