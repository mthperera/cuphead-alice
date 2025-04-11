import pygame
from constantes import *
from Classes.PlataformaXadrez import PlataformaXadrez
from Classes.PlataformaRainha import PlataformaRainha
from Classes.PlataformaRei import PlataformaRei

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


    def inicializa(self):
        pygame.init()

        # "Você é apenas uma peça... jogue ou seja descartada."

        window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), pygame.FULLSCREEN)

 
        return window


    def desenha(self, window):
        window.fill(BRANCO)
        
        window.blit(IMAGEM_FUNDO_RAINHA_VERMELHA, (0, 0))

        self.grupo_plataforma.draw(window)
        self.grupo_plataforma_rainha.draw(window)
        self.grupo_plataforma_rei.draw(window)

        pygame.display.flip()
    

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
        
        self.grupo_plataforma.update()
        self.grupo_plataforma_rainha.update()
        self.grupo_plataforma_rei.update()

        return True
    
    