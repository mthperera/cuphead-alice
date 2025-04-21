import pygame
from constantes import *
from Classes.Coelho import Coelho
from Classes.Alice.AliceCoelho import AliceCoelho
from random import choice


class TelaCoelho:

    def __init__(self):
        self.tela_atual = "TelaCoelho"
        self.nivel = 0
        self.coelho = Coelho()
        self.t0 = pygame.time.get_ticks()
        self.fundo = choice(LISTA_FUNDO_COELHO)
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)
        self.grupo_alice = pygame.sprite.Group()
        self.grupo_alice.add(AliceCoelho(400, ALTURA_TELA - 140))
        

    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(self.fundo, (0, 0))

        self.coelho.desenhar(window)
        self.grupo_alice.draw(window)

        pygame.display.flip()
    

    def atualiza_estado(self):
        
        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_COELHO, loops=-1)
            self.musica_tocando = True

        lista_eventos = pygame.event.get() 
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"

                
        self.coelho.movimentar()
        self.grupo_alice.update(lista_eventos)
        

        # Ponto em que o pulo do coelho começa:
        if self.coelho.pos_x > 2*LARGURA_TELA/5 and not self.coelho.pulo:
            self.coelho.pulo = True
            self.coelho.pos_y -= 30
            self.coelho.i = 0
            self.coelho.t0_pulo = pygame.time.get_ticks()
        
        for alice in self.grupo_alice:
            if alice.rect.x > 5.5 * LARGURA_TELA // 9:
                self.tela_atual = "TelaCartas"
                self.canal_0.stop()

        if not self.coelho.pulo:
            self.coelho.animar()
        else:
            self.coelho.pular()


        return True
    
