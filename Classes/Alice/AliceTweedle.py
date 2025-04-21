import pygame
from constantes import *
from Classes.Bolinho import Bolinho
from math import atan2, degrees, cos, sin, radians


class AliceTweedle(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.vidas = 5
        self.image = LISTA_ALICE_AVIAO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = (self.pos_x, self.pos_y))
        self.grupo_bolinhos = pygame.sprite.Group()
        self.t0 = pygame.time.get_ticks()
        self.t0_bolinho = self.t0_atacou_bolinho = pygame.time.get_ticks()
        self.t0_superbolo = self.t0_atacou_superbolo = pygame.time.get_ticks()
        self.t0_voar_movimentacao = self.t0_voar_animacao = pygame.time.get_ticks()
        self.velocidade = 300
        self.atacou_bolinho = self.atacando_bolinho = False
        self.atacou_superbolo = self.atacando_superbolo = False
        self.voando = False
        self.angulo = 0
        self.direcao = self.ultima_direcao = None
        self.t0_ultimo_dano = pygame.time.get_ticks()


    def ataque_bolinho(self):

        delta_t = pygame.time.get_ticks() - self.t0_bolinho
        indice = delta_t // 20
        if indice >= 6 and not self.atacou_bolinho:
            if not self.atacou_bolinho:
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho + 15))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, self.angulo_bolinho - 15))
                self.atacou_bolinho = True
                # fazer condições pro bolinho pra cada lado
        elif indice > 10:
            self.image = LISTA_ALICE_AVIAO[0]
            self.atacando_bolinho = False
            self.atacou_bolinho = False
            self.angulo_bolinho = 0
            if not self.atacando_bolinho and not self.atacando_superbolo:
                if hasattr(self, 'value_0') and abs(self.value_0) > 0.5:
                    self.angulo = 0 if self.value_0 > 0 else 180
                    if not self.voando:
                        self.t0_andar_movimentacao = self.t0_andar_animacao = pygame.time.get_ticks()
                    self.voando = True
                else:
                    self.voando = False
                    self.angulo = 0
        
        if 0 <= self.angulo_bolinho <= 90 or 270 <= self.angulo_bolinho <= 360:
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center = antigo_centro)
    

    def super_bolo(self):

        delta_t = pygame.time.get_ticks() - self.t0_superbolo
        indice = delta_t // 50
        if indice >= 7 and not self.atacou_superbolo:
            if not self.atacou_superbolo:
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 0))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 10))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 60))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 90))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 120))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 150))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 180))
                self.atacou_superbolo = True
        if indice > 10:
            self.atacando_superbolo = False
            self.atacou_superbolo = False


    def voar_movimentacao(self, angulo):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_voar_movimentacao) / 1000

        velocidade_x = self.velocidade * cos(radians(angulo))
        velocidade_y = self.velocidade * sin(radians(angulo))

        self.rect.x += velocidade_x * dt
        self.rect.y -= velocidade_y * dt

        self.t0_voar_movimentacao = now
        

    def voar_animacao(self, direcao):

        delta_t = (pygame.time.get_ticks() - self.t0_voar_animacao) % (200*13)
        indice = delta_t // 200
        self.image = LISTA_ALICE_AVIAO[indice]

        antigo_centro = self.rect.center
        if direcao == "Direita":
            self.image = pygame.transform.flip(self.image, True, False)
        elif direcao == "Esquerda":
            pass

        self.rect = self.image.get_rect(center = antigo_centro)


    def update(self, lista_eventos):

        for evento in lista_eventos:

            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis in [0, 1]:
                    if not self.voando:
                        self.t0_voar_movimentacao = pygame.time.get_ticks()
                        self.voando = True
                    if evento.axis == 0:
                        if evento.value > 0.5:
                            self.direcao = "Direita"
                        elif evento.value < -0.5:
                            self.direcao = "Esquerda"
                        self.value_0 = evento.value
                    if evento.axis == 1:
                        self.value_1 = evento.value
                else:
                    self.voando = False

                try:
                    if abs(self.value_0) < 0.2 and abs(self.value_1) < 0.2:
                        self.voando = False
                    else:
                        self.angulo = (degrees(atan2(-self.value_1, self.value_0)) + 360) % 360
                except AttributeError:
                    self.angulo = 90 if not hasattr(self, 'value_0') else 0
                    if not hasattr(self, 'value_0') and not hasattr(self, 'value_1'):
                        self.voando = False
                    elif not hasattr(self, 'value_0') and self.value_1 < 0.2:
                        self.voando = False
                    elif not hasattr(self, 'value_1') and self.value_0 < 0.2:
                        self.voando = False

            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 2 and pygame.time.get_ticks() - self.t0_atacou_bolinho > 1500:
                    self.atacando_bolinho = True
                    self.angulo_bolinho = self.angulo
                    self.t0_atacou_bolinho = self.t0_bolinho = pygame.time.get_ticks()
                if evento.button == 3 and pygame.time.get_ticks() - self.t0_atacou_superbolo > 4000:
                    self.atacando_superbolo = True
                    self.t0_atacou_superbolo = self.t0_superbolo = pygame.time.get_ticks()
            
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade = 400
                    else:
                        self.velocidade = 300

        self.voar_animacao(self.direcao)

        if self.atacando_bolinho:
            self.ataque_bolinho()
            
        if self.atacando_superbolo:
            self.super_bolo()
        
        if self.voando:
            if self.rect.left >= 0 and self.rect.right <= LARGURA_TELA and self.rect.bottom <= ALTURA_TELA and self.rect.top >= 0:
                self.voar_movimentacao(self.angulo)
            elif self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA_TELA:
                self.rect.right = LARGURA_TELA
            elif self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > ALTURA_TELA:
                self.rect.bottom = ALTURA_TELA

        
        self.mask = pygame.mask.from_surface(self.image)