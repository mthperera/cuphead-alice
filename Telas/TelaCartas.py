import pygame
from constantes import *

class TelaCartas():

    def __init__(self):
        self.t0 = pygame.time.get_ticks()


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(FUNDO_CARTAS, (0, 0))

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "Sair"


        return "TelaCartas"
    
    