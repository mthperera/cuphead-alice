# 1. Módulos de terceiros (pip)
import pygame

# 2. Módulos locais
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
from Telas.TelaVitoria import TelaVitoria
from Telas.TelaRanking import TelaRanking

# Esse método de telas foi escolhido para facilitar a troca de informações entre telas.
# Por exemplo, a passagem de nível que interfere na TelaCartas.
# Além disso, esse método ainda permite que a troca de tela, por exemplo,
# voltando para uma anterior seja feito por meio do: ' while self.tela_atual != "Sair" '.

class Jogo:
    """
    Essa classe é usada no jogo.py para dar o início. Ela basicamente faz o fluxo de telas.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel_atual (int): O nível do jogador.
        dano (int): O dano que o jogador causou nos chefões.
        tempo_iniciou (int): O tempo que o jogador começou.
        tempo_terminou (int): O tempo que o jogador terminou.
        window (Surface): Janela na qual tudo será desenhado.
        tela_inicial (TelaInicial): Instância da TelaInicial.
        nome (str): Nome do jogador.
    """
    
    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaCartas.

        Returns:
            None:
        """
        self.tela_atual = "TelaRainhaVermelha"
        self.nivel_atual = 0
        self.dano = 0
        self.tempo_iniciou = 0
        self.tempo_terminou = 0
        self.window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
        self.tela_inicial = TelaInicial()
        self.nome = None

    def inicializa(self) -> None:
        """
        Inicializa o jogo. Esse método gerencia e faz os fluxos de tela.

        Returns:
            None:
        """

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
                self.tempo_iniciou = pygame.time.get_ticks()//1000
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaCoelho":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
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
                        self.nivel_atual = tela.nivel
                        self.dano += tela.dano
                        break

            if self.tela_atual == "TelaTweedle":
                tela = TelaTweedle()
                tela.tela_atual = "TelaTweedle"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaTweedle":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        self.dano += tela.dano
                        break

            if self.tela_atual == "TelaRainhaVermelha":
                tela = TelaRainhaVermelha()
                tela.tela_atual = "TelaRainhaVermelha"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRainhaVermelha":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        self.nivel_atual = tela.nivel
                        self.dano += tela.dano
                        self.tempo_terminou = tela.tempo_terminou
                        break
            
            if self.tela_atual == "TelaGameOver":
                tela = TelaGameOver(nivel=self.nivel_atual)
                tela.tela_atual = "TelaGameOver"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaGameOver":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break
            
            if self.tela_atual == "TelaVitoria":
                tela = TelaVitoria(nivel=self.nivel_atual)
                tela.tela_atual = "TelaVitoria"
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaVitoria":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break
            
            if self.tela_atual == "TelaRanking":
                tela = TelaRanking(self.nome, self.nivel_atual, self.dano, self.tempo_iniciou, self.tempo_terminou)
                tela.tela_atual = "TelaRanking"
                tela.inicializa()
                while tela.atualiza_estado():
                    tela.desenha(self.window)
                    if tela.tela_atual != "TelaRanking":
                        pygame.event.clear()
                        self.tela_atual = tela.tela_atual
                        break
            

            if self.tela_atual == "Sair":
                break