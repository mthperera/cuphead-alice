import pygame
from constantes import *
from Classes.Coelho import Coelho

class TelaCoelho():

    def __init__(self):
        self.tela_atual = "TelaCoelho"
        self.coelho = Coelho()
        self.t0 = pygame.time.get_ticks()


    def inicializa(self):
        pygame.init()

        # info = pygame.display.Info()
        # largura, altura = info.current_w, info.current_h
        # window = pygame.display.set_mode((largura, altura), pygame.FULLSCREEN)

        window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
 
        return window


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(IMAGEM_FUNDO_COELHO, (0, 0))

        self.coelho.desenhar(window)

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
        
        
        self.coelho.movimentar()

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
    
    