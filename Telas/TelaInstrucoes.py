import pygame
from constantes import *

class TelaInstrucoes():

    def __init__(self):
        self.tela_atual = "TelaInstrucoes"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_INICAL[0]
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        # window.blit(self.fundo, (0, 0))

        pygame.display.flip()
    

    def atualiza_estado(self):
        
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"
            
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 1:
                    self.tela_atual = "TelaInicial"


        return True
    
    