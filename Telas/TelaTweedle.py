# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from Classes.Alice.AliceTweedle import AliceTweedle
from Classes.Tweedle import *
from Classes.PlataformaOvo import *
from Classes.Ioio import *

class TelaTweedle:
    """ 
    Representa a tela da Fase 2: Irmãos Tweedle.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        dano (int): O dano causado pelo jogador.
        grupo_alice (Group): Grupo de sprites da Alice.
        alice (AliceTweedle): Instância de AliceTweedle.
        grupo_tweedle (Group): Grupo de sprites dos Tweedle.
        grupo_plataformas_ovo (Group): Grupo de sprites das Plataformas de Ovo.
        grupo_ioios (Group): Grupo de sprites dos Ioio.
        tweedle_dee (TweedleDee): Instância de TweedleDee.
        tweedle_dum (TweedleDum): Instância de TweedleDum.
        plataforma_ovo_dee (PlataformaOvoDee): Instância de PlataformaOvoDee.
        plataforma_ovo_dum (PlataformaOvoDum): Instância de PlataformaOvoDum.
        ioio_dee (IoioDee): Instância de IoioDee.
        ioio_dum (IoioDum): Instância de IoioDum.
        t0 (int): O tempo em que a tela é iniciada.
        canal_0 (Channel): Canal utilizado para a música de fundo.
        canal_dano (Channel): Canal utilizado para a Alice levando dano.
        canal_acertou (Channel): Canal utilizado para Alice acertando um alvo.
        texto_vidas (Surface): Texto de vidas da Alice.
        texto_vidas_perdidas (Surface): Texto de vidas perdidas da Alice.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaTweedle. 

        Returns:
            None:
        """
        self.tela_atual = "TelaTweedle"
        self.nivel = 1
        self.dano = 0
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceTweedle(LARGURA_TELA//2, ALTURA_TELA//2)
        self.grupo_alice.add(self.alice)
        self.grupo_tweedle = pygame.sprite.Group()
        self.grupo_plataformas_ovo = pygame.sprite.Group()
        self.grupo_ioios = pygame.sprite.Group()
        self.tweedle_dee = TweedleDee(60, 20, self.alice)
        self.tweedle_dum = TweedleDum(LARGURA_TELA - LISTA_TEEDLE_OVO[0].get_width() - 60, 20, self.alice)
        self.plataforma_ovo_dee = PlataformaOvoDee(30, 110, self.tweedle_dee)
        self.plataforma_ovo_dum = PlataformaOvoDum(LARGURA_TELA - IMAGEM_CASCA_OVO.get_width() - 30, 110, self.tweedle_dum)
        self.ioio_dee = IoioDee(200, 450)
        self.ioio_dum = IoioDum(LARGURA_TELA - LISTA_IOIO[0].get_width() - 250, 450)
        self.grupo_tweedle.add(self.tweedle_dee)
        self.grupo_tweedle.add(self.tweedle_dum)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dee)
        self.grupo_plataformas_ovo.add(self.plataforma_ovo_dum)
        self.grupo_ioios.add(self.ioio_dee)
        self.grupo_ioios.add(self.ioio_dum)
        self.t0 = pygame.time.get_ticks()
        self.canal_0 = pygame.mixer.Channel(0)
        self.canal_dano = pygame.mixer.Channel(3)
        self.canal_acertou = pygame.mixer.Channel(4)
        self.texto_vidas = FONTE_CORACAO.render(CORACAO * self.alice.vidas, True, VERMELHO)
        self.texto_vidas_perdidas = FONTE_CORACAO.render(CORACAO * (5 - self.alice.vidas), True, BRANCO)

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo, os personagens, as cordas e as vidas.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_TWEEDLE, (0, 0))

        # Desenhando os Tweedle e as plataformas:
        self.grupo_plataformas_ovo.draw(window)
        self.grupo_tweedle.draw(window)

        # Desenhando "cordas" dos ioio:
        if self.tweedle_dee.vidas > 0:
            pygame.draw.line(window, MARROM, (self.ioio_dee.rect.x + 24, self.ioio_dee.rect.y + 5), (self.plataforma_ovo_dee.rect.x + 100, self.plataforma_ovo_dee.rect.y + 145), 3)
        if self.tweedle_dum.vidas > 0:
            pygame.draw.line(window, MARROM, (self.ioio_dum.rect.x + 24, self.ioio_dum.rect.y + 5), (self.plataforma_ovo_dum.rect.x + 100, self.plataforma_ovo_dum.rect.y + 145), 3)
        # Para ser mais realista, essa linha pode ser uma Catenária!

        # Desenhando os Ioio e os ovos:
        self.grupo_ioios.draw(window)
        self.tweedle_dee.grupo_ovos.draw(window)
        self.tweedle_dum.grupo_ovos.draw(window)
        
        # Desenhando a Alice e os bolinhos:
        self.grupo_alice.draw(window)
        self.alice.grupo_bolinhos.draw(window)

        # Desenhando as vidas da Alice:
        window.blit(QUADRO_VIDAS, (LARGURA_TELA//2 - QUADRO_VIDAS.get_width()//2 - 600, ALTURA_TELA - QUADRO_VIDAS.get_height() + 10))
        window.blit(self.texto_vidas, (LARGURA_TELA//2 - 47 - 600, ALTURA_TELA - 45))
        window.blit(self.texto_vidas_perdidas, (LARGURA_TELA//2 - 47 + self.alice.vidas * 20 - 600, ALTURA_TELA - 45))

        pygame.display.flip()

    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como música, eventos, personagens e colisões.

        Returns:
            bool: 
                - True se continuar na tela.
        """

        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            self.canal_0.play(MUSICA_FUNDO_TWEEDLE, loops=-1)

        # Verifica eventos de troca de tela ou saída do jogo:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"

        # Atualiza os Tweedle, a Alice, as plataformas, os bolinhos e os ioio:
        self.grupo_tweedle.update()
        self.grupo_plataformas_ovo.update()
        self.grupo_ioios.update()
        self.tweedle_dee.grupo_ovos.update()
        self.tweedle_dum.grupo_ovos.update()
        self.alice.update(lista_eventos)
        self.alice.grupo_bolinhos.update()
        
        if self.tweedle_dee in self.grupo_tweedle:

            # Verificando colisão entre Alice e os ovos:
            if pygame.sprite.spritecollide(self.alice, self.tweedle_dee.grupo_ovos, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                    if not self.canal_dano.get_busy():
                        self.canal_dano.play(SOM_ALICE_DANO, loops=0)
            
            # Verificando colisão entre TweedleDee e os bolinhos:
            if pygame.sprite.spritecollide(self.tweedle_dee, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dee.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verificando colisão entre a PlataformaDee e os bolinhos:
            if pygame.sprite.spritecollide(self.plataforma_ovo_dee, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dee.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verificando colisão entre os bolinhos e os ovos:
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.tweedle_dee.grupo_ovos, True, True, pygame.sprite.collide_mask):
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        
        if self.tweedle_dum in self.grupo_tweedle:

            # Verificando colisão entre a Alice e os ovos:
            if pygame.sprite.spritecollide(self.alice, self.tweedle_dum.grupo_ovos, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                    if not self.canal_dano.get_busy():
                        self.canal_dano.play(SOM_ALICE_DANO, loops=0)
            
            # Verificando colisão entre TweedleDum e os bolinhos:
            if pygame.sprite.spritecollide(self.tweedle_dum, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dum.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verificando colisão entre a PlataformaDum e os bolinhos:
            if pygame.sprite.spritecollide(self.plataforma_ovo_dum, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.tweedle_dum.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verificando colisão entre os bolinhos e os ovos:
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.tweedle_dum.grupo_ovos, True, True, pygame.sprite.collide_mask):
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        
        # Verificando colisão entre a alice e os ioio:
        if pygame.sprite.spritecollide(self.alice, self.grupo_ioios, False, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1500:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                    if not self.canal_dano.get_busy():
                        self.canal_dano.play(SOM_ALICE_DANO, loops=0)

        # Muda de tela quando os Tweedle morrem:
        if len(self.grupo_plataformas_ovo) == 0:
            self.canal_0.stop()
            self.tela_atual = "TelaVitoria"
            self.nivel = 2
            self.dano = 60

        # Termina o jogo quando a Alice morre:
        if self.alice.vidas <= 0:
            self.canal_0.stop()
            self.tela_atual = "TelaGameOver"
            self.nivel = 1
            self.dano = 30 - self.tweedle_dee.vidas + 30 - self.tweedle_dum.vidas
        
        # Atualizando os textos de vidas:
        self.texto_vidas = FONTE_CORACAO.render(CORACAO * self.alice.vidas, True, VERMELHO)
        self.texto_vidas_perdidas = FONTE_CORACAO.render(CORACAO * (5 - self.alice.vidas), True, BRANCO)

        return True

