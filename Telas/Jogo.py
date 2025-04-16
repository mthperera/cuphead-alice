import pygame
from constantes import *

from Telas.TelaNome import TelaNome
from Telas.TelaInicial import TelaInicial
from Telas.TelaInstrucoes import TelaInstrucoes
from Telas.TelaCoelho import TelaCoelho
from Telas.TelaRainhaCopas import TelaRainhaCopas
from Telas.TelaTweedle import TelaTweedle
from Telas.TelaRainhaVermelha import TelaRainhaVermelha
from Telas.TelaCartas import TelaCartas
from Telas.TelaGameOver import TelaGameOver


class Jogo():

    # Esse método de telas foi escolhido para facilitar a troca de informações entre telas.
    # Por exemplo, a passagem de nível que interfere na TelaCartas.
    # Além disso, esse método ainda permite que a troca de tela, por exemplo,
    # voltando para uma anterior seja feito por meio do: ' while self.tela_atual != "Sair" '.
    def __init__(self):
        self.tela_atual = "TelaCoelho"
        self.nivel_atual = 1
        self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.tela_inicial = TelaInicial()
        self.nome = None

    def inicializa(self):

        while self.tela_atual != "Sair":

            if self.tela_atual == "TelaNome":
                tela = TelaNome()
                tela.tela_atual = "TelaNome"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaNome":
                        pygame.event.clear()
                        self.nome = tela.nome
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaInicial":
                self.tela_inicial.tela_atual = "TelaInicial"
                while self.tela_inicial.atualiza_estado():
                    self.tela_inicial.desenha(self.window)
                    if self.tela_inicial.tela_atual != "TelaInicial":
                        pygame.event.clear()
                        self.tela_atual = self.tela_inicial.tela_atual
                        break
            
            if self.tela_atual == "TelaInstrucoes":
                tela = TelaInstrucoes()
                tela.tela_atual = "TelaInstrucoes"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaInstrucoes":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaCoelho":
                tela = TelaCoelho()
                tela.tela_atual = "TelaCoelho"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCoelho":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaCartas":
                tela = TelaCartas(nivel=self.nivel_atual)
                tela.tela_atual = "TelaCartas"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCartas":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        break

            if self.tela_atual == "TelaRainhaCopas":
                tela = TelaRainhaCopas()
                tela.tela_atual = "TelaRainhaCopas"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRainhaCopas":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaTweedle":
                tela = TelaTweedle()
                tela.tela_atual = "TelaTweedle"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaTweedle":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "TelaRainhaVermelha":
                tela = TelaRainhaVermelha()
                tela.tela_atual = "TelaRainhaVermelha"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRainhaVermelha":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break
            
            if self.tela_atual == "TelaGameOver":
                tela = TelaGameOver()
                tela.tela_atual = "TelaGameOver"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaGameOver":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break

            if self.tela_atual == "Sair":
                break