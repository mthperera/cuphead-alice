import pygame
from constantes import *

class TelaVitoria():

    def __init__(self, nivel):
        self.tela_atual = "TelaVitoria"
        self.t0 = pygame.time.get_ticks()
        self.nivel = nivel
        self.fundo = FUNDO_VITORIA[self.nivel - 1]
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(self.fundo, (0, 0))

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_GAMEOVER, loops=-1)
            self.musica_tocando = True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"
            
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.tela_atual = "TelaCartas"


        return True
    
    