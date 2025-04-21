import pygame
from constantes import *
from math import atan2, degrees


class AliceCoelho(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x, self.pos_y = (x, y)
        self.pos_y_inicial = self.pos_y
        self.image = LISTA_ALICE_SUPER_BOLO[0]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(midbottom = (self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
        self.t0_andar = self.t0_pular = self.t0_caindo = pygame.time.get_ticks()
        self.velocidade_x = 100
        self.velocidade_y = self.velocidade_y_inicial = -500
        self.aceleracao_y = 1000
        self.andando = self.pulando = False
        self.direcao = None
        self.canal_pulo = pygame.mixer.Channel(1)
    

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


    def pular_movimentacao(self, direcao):

        now = pygame.time.get_ticks()
        dt = (now - self.t0_pular_movimentacao) / 1000

        self.velocidade_y += self.aceleracao_y * dt
        self.rect.y += self.velocidade_y * dt
        if self.rect.bottom >= self.pos_y:
            self.rect.bottom = self.pos_y
            self.velocidade_y = self.velocidade_y_inicial
            self.pulando = False

        if self.rect.x > 0 and self.rect.x < LARGURA_TELA - 100:
            if direcao == "Direita":
                velocidade_x = self.velocidade_x
            elif direcao == "Esquerda":
                velocidade_x = -abs(self.velocidade_x)
            if direcao is not None:
                self.rect.x += velocidade_x * dt

        self.t0_pular_movimentacao = now

    
    def pular_animacao(self, direcao):

        delta_t = (pygame.time.get_ticks() - self.t0_pular_animacao) % (8*250)
        indice = delta_t // 250
        self.image = LISTA_ALICE_PULANDO[indice]
        
        if direcao == "Direita":
            antigo_centro = self.rect.center
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect = self.image.get_rect(center = antigo_centro)


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
                if evento.button == 0:
                    if not self.pulando:
                        self.t0_pular_animacao = self.t0_pular_movimentacao = pygame.time.get_ticks()
                        self.rect.y -= 1
                        self.canal_pulo.play(SOM_ALICE_PULO, loops=0)
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
        
        if self.andando:
            self.pulando = False
            if self.rect.left >= 0 and self.rect.right <= LARGURA_TELA:
                self.andar(self.direcao)
            elif self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > LARGURA_TELA:
                self.rect.right = LARGURA_TELA 
        
        if not self.andando and not self.pulando:
            self.image = LISTA_ALICE_SUPER_BOLO[0]
        
        if self.rect.bottom < self.pos_y:
            self.pular_movimentacao(self.direcao)

        
        self.mask = pygame.mask.from_surface(self.image)