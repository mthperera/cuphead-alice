import pygame
from constantes import *
from Classes.Coelho import Coelho
from random import choice

class TelaCoelho():

    def __init__(self):
        self.tela_atual = "TelaCoelho"
        self.coelho = Coelho()
        self.t0 = pygame.time.get_ticks()
        self.fundo = choice(LISTA_FUNDO_COELHO)
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(self.fundo, (0, 0))

        self.coelho.desenhar(window)

        pygame.display.flip()
    

    def atualiza_estado(self):
        
        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_COELHO, loops=-1)
            self.musica_tocando = True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"
        
        
        self.coelho.movimentar()

        # Ponto em que o pulo do coelho começa:
        if self.coelho.pos_x > 2*LARGURA_TELA/5 and not self.coelho.pulo:
            self.coelho.pulo = True
            self.coelho.pos_y -= 30
            self.coelho.i = 0
            self.coelho.t0_pulo = pygame.time.get_ticks()

        if not self.coelho.pulo:
            self.coelho.animar()
        else:
            self.coelho.pular()


        return True
    
    