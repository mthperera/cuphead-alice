import pygame
from random import randint
from constantes import *
from Classes.Plataforma import Plataforma
from Classes.Tweedle import *
from Classes.PlataformaOvo import *
from Classes.Ioio import *

class TelaTweedle:
    def __init__(self):
        self.tela_atual = "TelaTweedle"
        self.grupo_plataformas = pygame.sprite.Group()
        self.grupo_tweedle = pygame.sprite.Group()
        self.grupo_plataformas_ovo = pygame.sprite.Group()
        self.grupo_ioios = pygame.sprite.Group()
        self.tweedle_dee = TweedleDee(60, 20)
        self.tweedle_dum = TweedleDum(LARGURA_TELA - LISTA_TEEDLE_OVO[0].get_width() - 60, 20)
        self.plataforma_ovo_dee = PlataformaOvoDee(30, 110)
        self.plataforma_ovo_dum = PlataformaOvoDum(LARGURA_TELA - IMAGEM_CASCA_OVO.get_width() - 30, 110)
        self.ioio_dee = IoioDee(150, 350)
        self.ioio_dum = IoioDum(LARGURA_TELA - LISTA_IOIO[0].get_width() - 150, 350)
        self.grupo_tweedle.add(self.tweedle_dee)
        self.grupo_tweedle.add(self.tweedle_dum)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dee)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dum)
        self.grupo_ioios.add(self.ioio_dee)
        self.grupo_ioios.add(self.ioio_dum)
        self.t0 = pygame.time.get_ticks()
        self.delta_t = 1500


    def inicializa(self):
        pygame.init()
        # Animações ovo quebrando + sonoros estilo retro

        window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

        return window

    def desenha(self, window):
        window.fill(BRANCO)

        window.blit(IMAGEM_FUNDO_DRAGAO, (0, 0))

        self.grupo_plataformas.draw(window)
        self.grupo_plataformas_ovo.draw(window)
        self.grupo_tweedle.draw(window)
        pygame.draw.line(window, MARROM, (self.ioio_dee.rect.x + 24, self.ioio_dee.rect.y + 5), (self.plataforma_ovo_dee.rect.x + 100, self.plataforma_ovo_dee.rect.y + 145), 3)
        pygame.draw.line(window, MARROM, (self.ioio_dum.rect.x + 24, self.ioio_dum.rect.y + 5), (self.plataforma_ovo_dum.rect.x + 100, self.plataforma_ovo_dum.rect.y + 145), 3)
        # Para ser mais realista, essa linha pode ser uma Catenária!
        self.grupo_ioios.draw(window)
        for tweedle in self.grupo_tweedle:
            tweedle.grupo_ovos.draw(window)

        pygame.display.flip()

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return False
        

        self.grupo_plataformas.update()
        self.grupo_tweedle.update()
        self.grupo_plataformas_ovo.update()
        self.grupo_ioios.update()
        for tweedle in self.grupo_tweedle:
            tweedle.grupo_ovos.update()

        
        if (pygame.time.get_ticks() - self.t0) // self.delta_t > 0:
            numero = randint(1, 3)
            if numero in [1, 3]:
                x_1 = randint(350, LARGURA_TELA//3 - 96)
                x_2 = randint(LARGURA_TELA//3, 2* LARGURA_TELA//3 - 96)
                x_3 = randint(2*LARGURA_TELA//3, LARGURA_TELA - 446)
                y = -120

                self.grupo_plataformas.add(Plataforma(x_1, y))
                self.grupo_plataformas.add(Plataforma(x_2, y))
                self.grupo_plataformas.add(Plataforma(x_3, y))
            else:
                x_1 = randint(350, LARGURA_TELA//2 - 96)
                x_2 = randint(LARGURA_TELA//2, LARGURA_TELA - 350)
                y = -120

                self.grupo_plataformas.add(Plataforma(x_1, y))
                self.grupo_plataformas.add(Plataforma(x_2, y))
            
            self.delta_t += 1500
        

        return True

