from constantes import *
from math import sqrt, atan, degrees

class Coelho():
    
    def __init__(self):
        self.pos_x = 20
        self.pos_y_inicial = self.pos_y = ALTURA_TELA - 275 - (170-128)
        self.t0 = self.t0_inicio = self.t0_pulo = pygame.time.get_ticks()
        self.pulo = False
        self.velocidade_x = 70
        self.velocidade_y = -90
        self.aceleracao_y = 40

    def movimentar(self):
        self.t1 = pygame.time.get_ticks()
        self.dt = (self.t1 - self.t0)/1000

        self.pos_x += self.velocidade_x * self.dt

        self.t0 = self.t1
    
    def animar(self):

        if (pygame.time.get_ticks() - self.t0_inicio) %  500 <= 250:
            self.image = LISTA_COELHO_CORRENDO[0]
        elif (pygame.time.get_ticks() - self.t0_inicio) %  500 <= 500:
            self.image = LISTA_COELHO_CORRENDO[1]


    def pular(self):

        self.t1 = pygame.time.get_ticks()
        self.dt_pulo = (self.t1 - self.t0_pulo)/1000

        self.velocidade_y += self.aceleracao_y * self.dt_pulo
        self.pos_y += self.velocidade_y * self.dt_pulo

        if self.pos_y > self.pos_y_inicial - 30:
            self.velocidade_x = 40
            self.image.set_alpha(255- self.i*20)
            self.i += 1
        else:
            self.image = LISTA_COELHO_PULANDO[0]
            self.angulo = degrees(atan(self.velocidade_x/sqrt(self.velocidade_x**2 + self.velocidade_y**2)))
            self.image = pygame.transform.rotate(self.image, self.angulo)
        
        if self.pos_y > LARGURA_TELA + 10:
            self.pos_y = LARGURA_TELA + 10
            self.velocidade_y = 0
            self.aceleracao_y = 0

        self.t0_pulo = self.t1


    def desenhar(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))



