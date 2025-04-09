from Telas.TelaRainhaCopas import TelaRainhaCopas
from Telas.TelaCoelho import TelaCoelho


class Jogo():
    def __init__(self):
        self.tela_atual = "TelaCoelho"


    def inicializa(self):

        if self.tela_atual == "TelaRainhaCopas":
            rainha_copas = TelaRainhaCopas()
            window = rainha_copas.inicializa()
            while rainha_copas.atualiza_estado():
                rainha_copas.desenha(window)
                if rainha_copas.tela_atual != "TelaRainhaCopas":
                    self.tela_atual = rainha_copas.tela_atual
                    break

        if self.tela_atual == "TelaCoelho":
            tela_coelho = TelaCoelho()
            window = tela_coelho.inicializa()
            while tela_coelho.atualiza_estado():
                tela_coelho.desenha(window)
                if tela_coelho.tela_atual != "TelaCoelho":
                    self.tela_atual = tela_coelho.tela_atual
                    break
        

