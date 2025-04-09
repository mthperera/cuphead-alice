from Telas.TelaRainhaCopas import TelaRainhaCopas


class Jogo():
    def __init__(self):
        self.tela_atual = "TelaRainhaCopas"


    def inicializa(self):

        if self.tela_atual == "TelaRainhaCopas":
            rainha_copas = TelaRainhaCopas()
            window = rainha_copas.inicializa()
            while rainha_copas.atualiza_estado():
                rainha_copas.desenha(window)
                if rainha_copas.tela_atual != "TelaRainhaCopas":
                    self.tela_atual = rainha_copas.tela_atual
                    break
