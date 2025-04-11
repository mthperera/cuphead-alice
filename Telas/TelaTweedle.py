import pygame
from random import randint
from constantes import *
from Classes.Plataforma import Plataforma
from Classes.Ceu import *
from Classes.Tweedle import *
from Classes.PlataformaOvo import PlataformaOvo
from Classes.Ioio import *
from Classes.Ovo import Ovo

class TelaTweedle:
    def __init__(self):
        self.tela_atual = "TelaDragão"
        self.grupo_plataformas = pygame.sprite.Group()
        self.grupo_ceu = pygame.sprite.Group()
        self.grupo_tweedle = pygame.sprite.Group()
        self.grupo_plataformas_ovo = pygame.sprite.Group()
        self.grupo_ioios = pygame.sprite.Group()
        self.grupo_ovos = pygame.sprite.Group()
        self.ceu_01 = Ceu_01()
        self.ceu_02 = Ceu_02()
        self.tweedle_dee = TweedleDee(60, 20)
        self.plataforma_ovo_dee = PlataformaOvo(30, 110)
        self.ioio_dee = IoioDee(150, 350)
        self.grupo_ceu.add(self.ceu_01)
        self.grupo_ceu.add(self.ceu_02)
        self.grupo_tweedle.add(self.tweedle_dee)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dee)
        self.grupo_ioios.add(self.ioio_dee)
        self.t0 = pygame.time.get_ticks()
        self.delta_t = 1500


    def inicializa(self):
        pygame.init()

        window = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

        return window

    def desenha(self, window):
        window.fill(BRANCO)

        window.blit(IMAGEM_FUNDO_DRAGAO, (0, 0))


        # self.grupo_ceu.draw(window)

        self.grupo_plataformas.draw(window)
        self.grupo_plataformas_ovo.draw(window)
        self.grupo_tweedle.draw(window)
        # pygame.draw.line(window, MARROM, (self.ioio_dee.rect.x + 24, self.ioio_dee.rect.y + 5), (self.plataforma_ovo_dee.rect.x + 100, self.plataforma_ovo_dee.rect.y + 145), 5)
        self.grupo_ioios.draw(window)
        self.grupo_ovos.draw(window)

        pygame.display.flip()

    def atualiza_estado(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False

        self.grupo_plataformas.update()
        self.grupo_ceu.update()
        self.grupo_tweedle.update()
        self.grupo_plataformas_ovo.update()
        self.grupo_ioios.update()
        self.grupo_ovos.update()

        
        if (pygame.time.get_ticks() - self.t0) // self.delta_t > 0:
            if randint(1, 3) == 3:
                x_1 = randint(0, LARGURA_TELA//3 - 96)
                x_2 = randint(LARGURA_TELA//3, 2* LARGURA_TELA//3 - 96)
                x_3 = randint(2*LARGURA_TELA//3, LARGURA_TELA -96)
                y = -120

                self.grupo_plataformas.add(Plataforma(x_1, y))
                self.grupo_plataformas.add(Plataforma(x_2, y))
                self.grupo_plataformas.add(Plataforma(x_3, y))
            else:
                x_1 = randint(100, LARGURA_TELA//2 - 96)
                x_2 = randint(LARGURA_TELA//2, LARGURA_TELA - 100)
                y = -120

                self.grupo_plataformas.add(Plataforma(x_1, y))
                self.grupo_plataformas.add(Plataforma(x_2, y))
            
            self.delta_t += 1500
        
        for tweedle in self.grupo_tweedle:
            if tweedle.ovo_lancar:
                self.grupo_ovos.add(Ovo(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
                tweedle.ovo_lancado = True
                tweedle.ovo_lancar = False
        
        # if (pygame.time.get_ticks() - self.t0 - 30000) // self.delta_t_coracao > 0:
        #     for _ in range(12):
        #         coracao = Coracao()
        #         coracao.pos_y = randint(-700, -400)
        #         coracao.pos_x = randint(50, LARGURA_TELA - 100)
        #         self.lista_coracoes.append(coracao)
        #         self.rainha_copas.ataque_coracao = "Atacando"
        #         self.rainha_copas.t0_ataque = pygame.time.get_ticks()

        #     self.delta_t_coracao += 4000


        return True

