from constantes import *
import pygame
from math import cos, degrees, atan2
from Classes.Bolinho import Bolinho



class AliceRainhaVermelha(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.pos_y_inicial = self.pos_y
        self.vidas = 5
        self.image = LISTA_ALICE_SUPER_BOLO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom = (self.pos_x, self.pos_y))
        self.grupo_bolinhos = pygame.sprite.Group()
        self.t0 = pygame.time.get_ticks()
        self.t0_bolinho = self.t0_atacou_bolinho = pygame.time.get_ticks()
        self.t0_superbolo = self.t0_atacou_superbolo = pygame.time.get_ticks()
        self.t0_andar = self.t0_caindo = pygame.time.get_ticks()
        self.velocidade_x = 100
        self.atacou_bolinho = self.atacando_bolinho = False
        self.atacou_superbolo = self.atacando_superbolo = False
        self.andando = self.pulando = self.caindo = False
        self.direcao = None
        self.angulo = 0
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
        else:
            self.image = LISTA_ALICE_BOLINHO[indice]
        
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
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 30))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 60))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 90))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 120))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 150))
                self.grupo_bolinhos.add(Bolinho(self.rect.centerx, self.rect.centery, 180))
                self.atacou_superbolo = True
        if indice > 10:
            self.atacando_superbolo = False
            self.atacou_superbolo = False
        
        else:
            self.image = LISTA_ALICE_SUPER_BOLO[indice]


    def andar(self, direcao):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_andar_movimentacao) / 1000

        if direcao == "Direita":
            self.rect.x += self.velocidade_x * dt
        elif direcao == "Esquerda":
            self.rect.x -= self.velocidade_x * dt

        self.t0_andar_movimentacao = now
        

        delta_t = (pygame.time.get_ticks() - self.t0_andar_animacao) % (70*18)
        indice = delta_t // 70
        self.image = LISTA_ALICE_CORRENDO[indice]

        antigo_centro = self.rect.center
        if direcao == "Direita":
            self.image = pygame.transform.flip(self.image, True, False)
        
        elif direcao == "Esquerda":
            pass
        self.rect = self.image.get_rect(center = antigo_centro)


    def movimentar_plataforma(self):

        # Realizando MHS vertical:
        self.pos_y = self.pos_y_inicial + 10 * cos((pygame.time.get_ticks() - self.t0)/1000)
        self.rect.y = self.pos_y
    
    
    def cair(self):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_caindo)/1000

        self.rect.y += 200 * dt

        self.t0_caindo = now
    
    
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
                if evento.button == 2 and pygame.time.get_ticks() - self.t0_atacou_bolinho > 2000:
                    self.atacando_bolinho = True
                    self.angulo_bolinho = self.angulo
                    self.t0_atacou_bolinho = self.t0_bolinho = pygame.time.get_ticks()
                if evento.button == 3 and pygame.time.get_ticks() - self.t0_atacou_superbolo > 4000:
                    self.atacando_superbolo = True
                    self.t0_atacou_superbolo = self.t0_superbolo = pygame.time.get_ticks()


            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 5:
                    if evento.value > 0.7:
                        self.velocidade_x = 200
                    else:
                        self.velocidade_x = 150


        if self.atacando_bolinho:
            self.andando = False
            self.ataque_bolinho()
            
        if self.atacando_superbolo:
            self.super_bolo()
        
        if self.andando:
            if LARGURA_TELA//2 - 3.5*ALTURA_TELA//8 + 50 < self.rect.centerx < LARGURA_TELA//2 + 3.5*ALTURA_TELA//8 + 15:
                self.andar(self.direcao)
        
        if not (self.andando or self.atacando_bolinho or self.atacando_superbolo):
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        
        if self.rect.top > ALTURA_TELA:
            self.vidas = 0

        self.image = pygame.transform.scale(self.image, (128, 192))
        self.mask = pygame.mask.from_surface(self.image)