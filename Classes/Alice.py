import pygame
from constantes import *
from Classes.Bolinho import Bolinho
from math import atan2, degrees

class Alice(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.vidas = 5
        self.forca = 1
        self.image = LISTA_ALICE_SUPER_BOLO[0]
        self.rect = self.image.get_rect(midbottom = (self.pos_x, self.pos_y))
        self.grupo_bolinhos = pygame.sprite.Group()
        self.t0_bolinho = self.t0_atacou_bolinho = pygame.time.get_ticks()
        self.t0_superbolo = self.t0_atacou_superbolo = pygame.time.get_ticks()
        self.t0_andar = self.t0_pular = pygame.time.get_ticks()
        self.velocidade_x = 100
        self.velocidade_y = self.velocidade_y_inicial = -500
        self.aceleracao_y = 1000
        self.atacou_bolinho = self.atacando_bolinho = False
        self.atacou_superbolo = self.atacando_superbolo = False
        self.andando = self.pulando = False
        self.direcao = None 
        self.angulo = 0


    def ataque_bolinho(self):

        if (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 100:
            self.image = LISTA_ALICE_BOLINHO[0]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 200:
            self.image = LISTA_ALICE_BOLINHO[1]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 300:
            self.image = LISTA_ALICE_BOLINHO[2]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 400:
            self.image = LISTA_ALICE_BOLINHO[3]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 500:
            self.image = LISTA_ALICE_BOLINHO[4]
            if not self.atacou_bolinho:
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, self.angulo_bolinho))
                self.atacou_bolinho = True
            # fazer condições pro bolinho pra cada lado
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 750 < 600:
            self.image = LISTA_ALICE_BOLINHO[5]
        else:
            self.image = LISTA_ALICE_SUPER_BOLO[0]
            self.atacando_bolinho = False
            self.atacou_bolinho = False
            self.angulo_bolinho = 0
            if not self.pulando and not self.atacando_bolinho and not self.atacando_superbolo:
                if hasattr(self, 'value_0') and abs(self.value_0) > 0.5:
                    self.direcao = "Direita" if self.value_0 > 0 else "Esquerda"
                    if not self.andando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.andando = True
                else:
                    self.andando = False
                    self.direcao = None
        
        if 90 < self.angulo_bolinho < 270:
            self.image = pygame.transform.flip(self.image, True, False)
    

    def super_bolo(self):

        if (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 250:
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 500:
            self.image = LISTA_ALICE_SUPER_BOLO[1]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 750:
            self.image = LISTA_ALICE_SUPER_BOLO[2]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 1000:
            self.image = LISTA_ALICE_SUPER_BOLO[3]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 1250:
            self.image = LISTA_ALICE_SUPER_BOLO[4]
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 1500:
            self.image = LISTA_ALICE_SUPER_BOLO[5]
            if not self.atacou_superbolo:
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, 30))
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, 60))
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, 90))
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, -30))
                self.grupo_bolinhos.add(Bolinho(self.rect.x, self.rect.y, -60))
                self.atacou_superbolo = True
        elif (pygame.time.get_ticks() - self.t0_bolinho) % 2000 < 1750: 
            self.image = self.image = LISTA_ALICE_SUPER_BOLO[0]
            self.atacando_superbolo = False
            self.atacou_superbolo = False


    def andar(self, direcao):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_andar_movimentacao) / 1000

        if direcao == "Direita":
            self.rect.x += self.velocidade_x * dt
        elif direcao == "Esquerda":
            self.rect.x -= self.velocidade_x * dt

        self.t0_andar_movimentacao = now
        
        if (pygame.time.get_ticks() - self.t0_andar_animacao) % 750 < 125:
            self.image = LISTA_ALICE_CORRENDO[0]
        elif (pygame.time.get_ticks() - self.t0_andar_animacao) % 750 < 250:
            self.image = LISTA_ALICE_CORRENDO[1]
        elif (pygame.time.get_ticks() - self.t0_andar_animacao) % 750 < 375:
            self.image = LISTA_ALICE_CORRENDO[2]
        elif (pygame.time.get_ticks() - self.t0_andar_animacao) % 750 < 500:
            self.image = LISTA_ALICE_CORRENDO[3]
        elif (pygame.time.get_ticks() - self.t0_andar_animacao) % 750 < 625:
            self.image = LISTA_ALICE_CORRENDO[4]
        else:
            self.image = LISTA_ALICE_CORRENDO[0]

        if direcao == "Direita":
            self.image = pygame.transform.rotate(self.image, -10)
        elif direcao == "Esquerda":
            self.image = pygame.transform.rotate(self.image, -10)
            self.image = pygame.transform.flip(self.image, True, False)

    
    def pular_movimentacao(self, direcao):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_pular_movimentacao) / 1000

        self.velocidade_y += self.aceleracao_y * dt
        self.rect.y += self.velocidade_y * dt
        if self.rect.bottom >= self.pos_y:
            self.rect.bottom = self.pos_y
            self.velocidade_y = self.velocidade_y_inicial
            self.pulando = False

        if direcao == "Direita":
            velocidade_x = self.velocidade_x
        elif direcao == "Esquerda":
            velocidade_x = -abs(self.velocidade_x)
        if direcao is not None:
            self.rect.x += velocidade_x * dt

        self.t0_pular_movimentacao = now

    
    def pular_animacao(self, direcao):

        delta_t = (pygame.time.get_ticks() - self.t0_pular_animacao) % 2000
        indice = delta_t // 250 if delta_t < 1000 else -1 - (-1000 + delta_t) // 250
        self.image = LISTA_ALICE_PULANDO[indice]
        
        if direcao == "Direita":
            self.image = pygame.transform.flip(self.image, True, False)

    
    def update(self, lista_eventos):

        for evento in lista_eventos:

            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 0:
                    if not self.andando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.andando = True
                    if evento.value > 0.5:
                        self.direcao = "Direita"
                    elif evento.value < -0.5:
                        self.direcao = "Esquerda"
                    else:
                        self.direcao = None
                        self.andando = False
                    self.value_0 = evento.value
                elif evento.axis == 1:
                    self.value_1 = evento.value

                try:
                    self.angulo = (degrees(atan2(-self.value_1, self.value_0)) + 360) % 360
                except AttributeError:
                    self.angulo = 90 if not hasattr(self, 'value_0') else 0


            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 2 and pygame.time.get_ticks() - self.t0_atacou_bolinho > 1000:
                    self.atacando_bolinho = True
                    self.angulo_bolinho = self.angulo
                    self.t0_atacou_bolinho = pygame.time.get_ticks()
                if evento.button == 3 and pygame.time.get_ticks() - self.t0_atacou_superbolo > 5000:
                    self.atacando_superbolo = True
                    self.t0_atacou_superbolo = pygame.time.get_ticks()
                if evento.button == 0:
                    if not self.pulando:
                        self.t0_pular_animacao = self.t0_pular_movimentacao = pygame.time.get_ticks()
                        self.rect.y -= 1
                    self.pulando = True
            
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade_x = 200
                    else:
                        self.velocidade_x = 150

        if self.pulando:
            self.andando = False
            self.pular_animacao(self.direcao)

        if self.atacando_bolinho:
            self.pulando = self.andando = False
            self.ataque_bolinho()
            
        if self.atacando_superbolo:
            self.super_bolo()
        
        if self.andando:
            self.pulando = False
            self.andar(self.direcao)
        
        if not (self.andando or self.pulando or self.atacando_bolinho or self.atacando_superbolo):
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        
        if self.rect.bottom < self.pos_y:
            self.pular_movimentacao(self.direcao)