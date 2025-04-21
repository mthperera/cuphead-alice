import pygame
from constantes import *

class TelaCartas():

    def __init__(self, nivel):
        self.tela_atual = "TelaCartas"
        self.t0 = pygame.time.get_ticks()
        self.nivel = nivel
        self.dict_cartas_viradas = {
            LISTA_CARTA_VIRADA[0] : (9, 55),
            LISTA_CARTA_VIRADA[1] : (468, 55),
            LISTA_CARTA_VIRADA[2] : (880, 55),
        }
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(FUNDO_CARTAS, (0, 0))

        for i in range(self.nivel):
            window.blit(LISTA_CARTA_VIRADA[i], self.dict_cartas_viradas[LISTA_CARTA_VIRADA[i]])

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            MUSICA_FUNDO_CARTAS.set_volume(1.0)
            self.canal_0.play(MUSICA_FUNDO_CARTAS, loops=-1)
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
                    if self.nivel == 0:
                        self.tela_atual = "TelaRainhaCopas"
                    elif self.nivel == 1:
                        self.tela_atual = "TelaTweedle"
                    elif self.nivel == 2:
                        self.tela_atual = "TelaRainhaVermelha"
                    elif self.nivel == 3:
                        self.tela_atual = "TelaRanking"
                    self.canal_0.stop()



        return True
    
    