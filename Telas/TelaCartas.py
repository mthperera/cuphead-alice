import pygame
from constantes import *

class TelaCartas():

    def __init__(self, nivel):
        self.tela_atual = "TelaCartas"
        self.t0 = pygame.time.get_ticks()
        self.nivel = nivel
        self.dict_cartas_viradas = {
            LISTA_CARTA_VIRADA[0] : (-15, 13),
            LISTA_CARTA_VIRADA[1] : (445, 13),
            LISTA_CARTA_VIRADA[2] : (858, 13),
        }


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(FUNDO_CARTAS, (0, 0))

        for i in range(self.nivel):
            window.blit(LISTA_CARTA_VIRADA[i], self.dict_cartas_viradas[LISTA_CARTA_VIRADA[i]])

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"


        return True
    
    