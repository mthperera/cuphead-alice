import pygame
from constantes import *

from Telas.TelaRainhaCopas import TelaRainhaCopas
from Telas.TelaCoelho import TelaCoelho
from Telas.TelaTweedle import TelaTweedle
from Telas.TelaRainhaVermelha import TelaRainhaVermelha
from Telas.TelaCartas import TelaCartas


class Jogo():

    def __init__(self):
        self.tela_atual = "TelaCartas"
        self.nivel_atual = 0
        self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

    def inicializa(self):

        while self.tela_atual != "Sair":

            if self.tela_atual == "TelaCoelho":
                tela = TelaCoelho()
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCoelho":
                        self.tela_atual = tela.tela_atual
                        break
            
            if self.tela_atual == "TelaCartas":
                tela = TelaCartas(nivel=self.nivel_atual)
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCartas":
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        break
        
            if self.tela_atual == "TelaRainhaCopas":
                tela = TelaRainhaCopas()
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRainhaCopas":
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaCartas":
                tela = TelaCartas(nivel=self.nivel_atual)
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCartas":
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        break

            if self.tela_atual == "TelaTweedle":
                tela = TelaTweedle()
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaTweedle":
                        self.tela_atual = tela.tela_atual
                        break
            
            if self.tela_atual == "TelaCartas":
                tela = TelaCartas(nivel=self.nivel_atual)
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCartas":
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        break

            if self.tela_atual == "TelaRainhaVermelha":
                tela = TelaRainhaVermelha()
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRainhaVermelha":
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaCartas":
                tela = TelaCartas(nivel=self.nivel_atual)
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCartas":
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        break
            
            if self.tela_atual == "Sair":
                break







# class Jogo():

#     def __init__(self):
#         self.tela_atual_key = "TelaCartas"
#         self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
#         self.telas = {
#             "TelaRainhaCopas": TelaRainhaCopas(),
#             "TelaCoelho": TelaCoelho(),
#             "TelaRainhaVermelha": TelaRainhaVermelha(),
#             "TelaTweedle": TelaTweedle(),
#             "TelaCartas": TelaCartas(),
#             "Sair": "Sair"
#         }
#         self.tela_atual_value = self.telas[self.tela_atual_key]


#     def inicializa(self):
#         # vai dar problema no t0 quando mudar de tela pq a classe foi inicializada antes. caso uma fase fosse se repetir, todos os parâmetros não iriam estar zerados, ai seria mt paia, talvez seja legal inicializar no looping

#         while self.tela_atual_key in [key for key in self.telas.keys() if key != "Sair"]:
#             self.tela_atual_value.desenha(self.window)
#             self.proxima_tela = self.tela_atual_value.atualiza_estado()
#             if self.proxima_tela != self.tela_atual_key:
#                 self.tela_atual_key = self.proxima_tela
#                 self.tela_atual_value = self.telas[self.tela_atual_key]







