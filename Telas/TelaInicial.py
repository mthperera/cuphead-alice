import pygame
from constantes import *

class TelaInicial():

    def __init__(self):
        self.tela_atual = "TelaInicial"
        self.proxima_tela = "TelaCoelho"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_INICAL[0]
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(self.fundo, (0, 0))

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_ALICE, loops=-1)
            self.musica_tocando = True
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair" 
                
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 1:
                    if evento.value < - 0.8:
                        self.proxima_tela = "TelaCoelho"
                        self.fundo = FUNDO_TELA_INICAL[0]
                    if evento.value > 0.8:
                        self.proxima_tela = "TelaInstrucoes"
                        self.fundo = FUNDO_TELA_INICAL[1]
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.tela_atual = self.proxima_tela
                    if self.proxima_tela == "TelaCoelho":
                        self.canal_0.stop()


        return True
    
    