from Telas.TelaRainhaCopas import TelaRainhaCopas
from Telas.TelaCoelho import TelaCoelho
from Telas.TelaTweedle import TelaTweedle


class Jogo():

    def __init__(self):
        self.tela_atual = "TelaDragão"


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
        
        if self.tela_atual == "TelaDragão":
            tela_tweedle = TelaTweedle()
            window = tela_tweedle.inicializa()
            while tela_tweedle.atualiza_estado():
                tela_tweedle.desenha(window)
                if tela_tweedle.tela_atual != "TelaDragão":
                    self.tela_atual = tela_tweedle.tela_atual
                    break
        

