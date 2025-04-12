import pygame
from constantes import *
from Classes.PlataformaXadrez import PlataformaXadrez
from Classes.PlataformaRainha import PlataformaRainha
from Classes.PlataformaRei import PlataformaRei
from Classes.RainhaVermelha import RainhaVermelha
from Classes.ReiVermelho import ReiVermelho

class TelaRainhaVermelha():

    def __init__(self):
        self.tela_atual = "TelaRainhaVermelha"
        self.t0 = pygame.time.get_ticks()
        self.grupo_plataforma = pygame.sprite.Group()
        self.grupo_plataforma.add(PlataformaXadrez())
        self.grupo_plataforma_rainha = pygame.sprite.Group()
        self.grupo_plataforma_rainha.add(PlataformaRainha())
        self.grupo_plataforma_rei = pygame.sprite.Group()
        self.grupo_plataforma_rei.add(PlataformaRei())
        self.grupo_rainha = pygame.sprite.Group()
        self.grupo_rainha.add(RainhaVermelha(LARGURA_TELA - 210, 68))
        self.grupo_rei = pygame.sprite.Group()
        self.grupo_rei.add(ReiVermelho(50, 70))

        # "Você é apenas uma peça... jogue ou seja descartada."


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(IMAGEM_FUNDO_RAINHA_VERMELHA, (0, 0))
        window.blit(IMAGEM_RAINHA_BRANCA, (LARGURA_TELA//2 - IMAGEM_RAINHA_BRANCA.get_width()//2, 0))

        self.grupo_plataforma.draw(window)
        self.grupo_plataforma_rainha.draw(window)
        self.grupo_plataforma_rei.draw(window)
        self.grupo_rainha.draw(window)
        self.grupo_rei.draw(window)
        for rainha in self.grupo_rainha:
            rainha.grupo_livros.draw(window)
        for rei in self.grupo_rei:
            rei.grupo_pecas.draw(window)
        

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"
        
        self.grupo_plataforma.update()
        self.grupo_plataforma_rainha.update()
        self.grupo_plataforma_rei.update()
        self.grupo_rainha.update()
        self.grupo_rei.update()
        for rainha in self.grupo_rainha:
            rainha.grupo_livros.update()
        for rei in self.grupo_rei:
            rei.grupo_pecas.update()

        return True
    
    