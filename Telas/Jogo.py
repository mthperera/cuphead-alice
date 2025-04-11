from Telas.TelaRainhaCopas import TelaRainhaCopas
from Telas.TelaCoelho import TelaCoelho
from Telas.TelaTweedle import TelaTweedle
from Telas.TelaRainhaVermelha import TelaRainhaVermelha


class Jogo():

    def __init__(self):
        self.tela_atual = "TelaRainhaVermelha"


    def inicializa(self):

        if self.tela_atual == "TelaRainhaCopas":
            tela_rainha_copas = TelaRainhaCopas()
            window = tela_rainha_copas.inicializa()
            while tela_rainha_copas.atualiza_estado():
                tela_rainha_copas.desenha(window)
                if tela_rainha_copas.tela_atual != "TelaRainhaCopas":
                    self.tela_atual = tela_rainha_copas.tela_atual
                    break

        if self.tela_atual == "TelaCoelho":
            tela_coelho = TelaCoelho()
            window = tela_coelho.inicializa()
            while tela_coelho.atualiza_estado():
                tela_coelho.desenha(window)
                if tela_coelho.tela_atual != "TelaCoelho":
                    self.tela_atual = tela_coelho.tela_atual
                    break
        
        if self.tela_atual == "TelaTweedle":
            tela_tweedle = TelaTweedle()
            window = tela_tweedle.inicializa()
            while tela_tweedle.atualiza_estado():
                tela_tweedle.desenha(window)
                if tela_tweedle.tela_atual != "TelaTweedle":
                    self.tela_atual = tela_tweedle.tela_atual
                    break
        
        if self.tela_atual == "TelaRainhaVermelha":
            tela_rainha_vermelha = TelaRainhaVermelha()
            window = tela_rainha_vermelha.inicializa()
            while tela_rainha_vermelha.atualiza_estado():
                tela_rainha_vermelha.desenha(window)
                if tela_rainha_vermelha.tela_atual != "TelaRainhaVermelha":
                    self.tela_atual = tela_rainha_vermelha.tela_atual
                    break
        

