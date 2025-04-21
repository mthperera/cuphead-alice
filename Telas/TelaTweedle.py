import pygame
from random import choice
from constantes import *
from Classes.Alice.AliceTweedle import AliceTweedle
from Classes.Tweedle import *
from Classes.PlataformaOvo import *
from Classes.Ioio import *

class TelaTweedle:
    def __init__(self):
        self.tela_atual = "TelaTweedle"
        self.nivel = 1
        self.dano = 0
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceTweedle(LARGURA_TELA//2, ALTURA_TELA//2)
        self.alice.tela_atual = "TelaRainhaVermelha"
        self.grupo_alice.add(self.alice)
        self.grupo_tweedle = pygame.sprite.Group()
        self.grupo_plataformas_ovo = pygame.sprite.Group()
        self.grupo_ioios = pygame.sprite.Group()
        self.tweedle_dee = TweedleDee(60, 20, self.alice)
        self.tweedle_dum = TweedleDum(LARGURA_TELA - LISTA_TEEDLE_OVO[0].get_width() - 60, 20, self.alice)
        self.plataforma_ovo_dee = PlataformaOvoDee(30, 110)
        self.plataforma_ovo_dum = PlataformaOvoDum(LARGURA_TELA - IMAGEM_CASCA_OVO.get_width() - 30, 110)
        self.ioio_dee = IoioDee(200, 450)
        self.ioio_dum = IoioDum(LARGURA_TELA - LISTA_IOIO[0].get_width() - 250, 450)
        self.grupo_tweedle.add(self.tweedle_dee)
        self.grupo_tweedle.add(self.tweedle_dum)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dee)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dum)
        self.grupo_ioios.add(self.ioio_dee)
        self.grupo_ioios.add(self.ioio_dum)
        self.t0 = pygame.time.get_ticks()
        self.delta_t = 1500
        self.musica_tocando = False
        self.canal_0 = pygame.mixer.Channel(0)


    def desenha(self, window):
        window.fill(BRANCO)

        window.blit(IMAGEM_FUNDO_TWEEDLE, (0, 0))

        self.grupo_plataformas_ovo.draw(window)
        self.grupo_tweedle.draw(window)

        # Desenhando "cordas" dos ioio"
        pygame.draw.line(window, MARROM, (self.ioio_dee.rect.x + 24, self.ioio_dee.rect.y + 5), (self.plataforma_ovo_dee.rect.x + 100, self.plataforma_ovo_dee.rect.y + 145), 3)
        pygame.draw.line(window, MARROM, (self.ioio_dum.rect.x + 24, self.ioio_dum.rect.y + 5), (self.plataforma_ovo_dum.rect.x + 100, self.plataforma_ovo_dum.rect.y + 145), 3)
        # Para ser mais realista, essa linha pode ser uma Catenária!

        self.grupo_ioios.draw(window)
        for tweedle in self.grupo_tweedle:
            tweedle.grupo_ovos.draw(window)
        
        self.grupo_alice.draw(window)
        self.alice.grupo_bolinhos.draw(window)

        pygame.display.flip()


    def atualiza_estado(self):

        if not self.musica_tocando:
            self.canal_0.play(MUSICA_FUNDO_TWEEDLE, loops=-1)
            self.musica_tocando = True


        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"
        
        
        if self.tweedle_dee in self.grupo_tweedle:
            if pygame.sprite.spritecollide(self.alice, self.tweedle_dee.grupo_ovos, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    print("ovo_dee")
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
            if pygame.sprite.spritecollide(self.tweedle_dee, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dee.vidas -= 1
            if pygame.sprite.spritecollide(self.plataforma_ovo_dee, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dee.vidas -= 1
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.tweedle_dee.grupo_ovos, True, True, pygame.sprite.collide_mask):
                pass
        
        if self.tweedle_dum in self.grupo_tweedle:
            if pygame.sprite.spritecollide(self.alice, self.tweedle_dum.grupo_ovos, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    print("ovo_dum")
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
            if pygame.sprite.spritecollide(self.tweedle_dum, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dum.vidas -= 1
            if pygame.sprite.spritecollide(self.plataforma_ovo_dum, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dum.vidas -= 1
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.tweedle_dum.grupo_ovos, True, True, pygame.sprite.collide_mask):
                pass
        
        if pygame.sprite.spritecollide(self.alice, self.grupo_ioios, False, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1500:
                    self.alice.vidas -= 1
                    print("ioio")
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()


        self.grupo_tweedle.update()
        self.grupo_plataformas_ovo.update()
        self.grupo_ioios.update()
        for tweedle in self.grupo_tweedle:
            tweedle.grupo_ovos.update()
        
        self.alice.update(lista_eventos)
        self.alice.grupo_bolinhos.update()

        if self.alice.vidas <= 0:
            self.tela_atual = "TelaGameOver"
            self.nivel = 1
            self.dano = 30 - self.tweedle_dee.vidas + 30 - self.tweedle_dum.vidas
        
        if len(self.grupo_tweedle)== 0:
            self.tela_atual = "TelaCartas"
            self.nivel = 2
            self.dano = 60


        return True

