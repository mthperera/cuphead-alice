from constantes import *
from math import cos
import pygame
from Classes.Cartinha import Cartinha
from Classes.Coracao import Coracao

class RainhaCopas(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = LISTA_INVOCAR_CORACAO[2]
        self.grupo_cartinhas = pygame.sprite.Group()
        self.grupo_coracoes = pygame.sprite.Group()
        self.t0_movimento = self.t0 = pygame.time.get_ticks()
        self.pos_x_inicial = LARGURA_TELA - 300
        self.pos_x = self.pos_x_inicial
        self.pos_y_inicial = ALTURA_TELA - 315
        self.pos_y = self.pos_y_inicial
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.ataque_coracao = "Sem ataque"
        self.t0_ataque = 0
        self.delta_t_remove = 15000
        self.delta_t_acel = 5000
        self.delta_t_coracao = 5000
        self.vida = 30
        self.dano = 1
    

    def invocar_coracoes(self):

        # Animação de invocar corações:
        if (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 250:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 500:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 750:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 1000:
            self.image = LISTA_INVOCAR_CORACAO[3]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 1250:
            self.image = LISTA_INVOCAR_CORACAO[4]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 1500:
            self.image = LISTA_INVOCAR_CORACAO[5]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 1750:
            self.image = LISTA_INVOCAR_CORACAO[6]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 2000:
            self.image = LISTA_INVOCAR_CORACAO[5]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 2250:
            self.image = LISTA_INVOCAR_CORACAO[4]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 2500:
            self.image = LISTA_INVOCAR_CORACAO[3]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 2750:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 3000:
            self.image = LISTA_INVOCAR_CORACAO[2]
        elif (pygame.time.get_ticks() - self.t0_ataque) %  6000 <= 3250:
            self.image = LISTA_INVOCAR_CORACAO[2] 
        else:
            self.vivo = "Sem ataque"
            self.image = LISTA_INVOCAR_CORACAO[2]
    

    def movimentar(self):
        # Figura de Lissajous -> maior sensação de movimentação real:
        self.rect.x = self.pos_x_inicial + 50*cos(1*(pygame.time.get_ticks()-self.t0_movimento)/1000)
        self.rect.y = self.pos_y_inicial + 3*cos(2*(pygame.time.get_ticks()-self.t0_movimento)/1000)


    def update(self):

        # Spawnando cartinhas a cada self.delta_t_acel ms:
        if (pygame.time.get_ticks() - self.t0) // self.delta_t_acel > 0 and (pygame.time.get_ticks()- self.t0) < 100000:
            for _ in range(5):
                cartinha = Cartinha()
                self.grupo_cartinhas.add(cartinha)

            self.delta_t_acel += 5000
        
        # Spawnando coracoes a cada self.delta_t_coracao ms:
        if (pygame.time.get_ticks() - self.t0 - 30000) // self.delta_t_coracao > 0:
            self.ataque_coracao = "Atacando"
            for _ in range(14):
                coracao = Coracao()
                self.grupo_coracoes.add(coracao)
                self.t0_ataque = pygame.time.get_ticks()

            self.delta_t_coracao += 6000
        
        # Matando cartinhas em excesso:
        if (pygame.time.get_ticks() - self.t0) // self.delta_t_remove > 0 and (pygame.time.get_ticks() - self.t0) < 100000:
            if len(self.grupo_cartinhas) > 3:
                i=0
                for cartinha in self.grupo_cartinhas:
                    if i > 3:
                        break
                    cartinha.vivo = "Morrendo"
                    cartinha.t0_morte = pygame.time.get_ticks()
                    i += 1

                    self.delta_t_remove += 10000


        self.movimentar()
        if self.ataque_coracao == "Atacando":
                self.invocar_coracoes()