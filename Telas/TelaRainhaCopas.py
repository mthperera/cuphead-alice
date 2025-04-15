from Classes.Cartinha import Cartinha
from Classes.Coracao import Coracao
from Classes.RainhaCopas import RainhaCopas
from constantes import *

class TelaRainhaCopas():

    def __init__(self):
        self.tela_atual = "TelaRainhaCopas"
        self.grupo_rainha = pygame.sprite.Group()
        self.grupo_rainha.add(RainhaCopas())
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_RAINHA_COPAS, (0, 0))
        
        for rainha in self.grupo_rainha:
            rainha.grupo_cartinhas.draw(window)
            rainha.grupo_coracoes.draw(window)

        self.grupo_rainha.draw(window)

        pygame.display.flip()
    

    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_RAINHA_COPAS, loops=-1)
            self.musica_tocando = True

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"


        self.grupo_rainha.update()

        for rainha in self.grupo_rainha:
            for cartinha in rainha.grupo_cartinhas:
                if cartinha.vivo == "Vivo":
                    cartinha.movimentar_acelerando(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    cartinha.rotacionar()
            rainha.grupo_cartinhas.update()
            rainha.grupo_coracoes.update()

        return True
    
    