# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaCopas import AliceRainhaCopas
from Classes.RainhaCopas import RainhaCopas


def verifica_colisao(entidade_1: pygame.sprite.Sprite, entidade_2: pygame.sprite.Sprite) -> bool:
    """
    Testa colisão entre duas sprites.

    Args:
        entidade_1 (pygame.sprite.Sprite) : Entidade 1.
        entidade_2 (pygame.sprite.Sprite) : Entidade 2.
    
    Returns:
        bool:
    """
    delta_x = entidade_2.rect.x - entidade_1.rect.x
    delta_y = entidade_2.rect.y - entidade_1.rect.y

    if entidade_2.mask.overlap(entidade_1.mask, (delta_x, delta_y)) is None:
        return False
    
    return True


class TelaRainhaCopas:
    """ 
    Representa a tela da Fase 1: Rainha de Copas.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        dano (int): O dano causado pelo jogador.
        grupo_alice (Group): Grupo de sprites da Alice.
        alice (AliceRainhaCopas): Instância de AliceRainhaCopas.
        grupo_rainha (Group): Grupo de sprites da RainhaCopas.
        rainha (RainhaCopas): Instância de RainhaCopas.
        canal_0 (Channel): Canal utilizado para a música de fundo.
        canal_dano (Channel): Canal utilizado para a Alice levando dano.
        canal_acertou (Channel): Canal utilizado para Alice acertando um alvo.
        texto_vidas (Surface): Texto de vidas da Alice.
        texto_vidas_perdidas (Surface): Texto de vidas perdidas da Alice.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaRainhaCopas. 

        Returns:
            None:
        """
        self.tela_atual = "TelaRainhaCopas"
        self.nivel = 0
        self.dano = 0
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceRainhaCopas(400, ALTURA_TELA - 50)
        self.grupo_alice.add(self.alice)
        self.grupo_rainha = pygame.sprite.Group()
        self.rainha = RainhaCopas(self.alice)
        self.grupo_rainha.add(self.rainha)
        self.canal_0 = pygame.mixer.Channel(0)
        self.canal_dano = pygame.mixer.Channel(3)
        self.canal_acertou = pygame.mixer.Channel(4)
        self.texto_vidas = FONTE_CORACAO.render(CORACAO * self.alice.vidas, True, VERMELHO)
        self.texto_vidas_perdidas = FONTE_CORACAO.render(CORACAO * (5 - self.alice.vidas), True, BRANCO)

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo, os personagens e as vidas.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_RAINHA_COPAS, (0, 0))
        
        # Desenhando os personagens:
        self.grupo_rainha.draw(window)
        for rainha in self.grupo_rainha:
            rainha.grupo_cartinhas.draw(window)
            rainha.grupo_coracoes.draw(window)
        self.grupo_alice.draw(window)
        for alice in self.grupo_alice:
            alice.grupo_bolinhos.draw(window)

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
            self.canal_0.play(MUSICA_FUNDO_RAINHA_COPAS, loops=-1)

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

        # Atualiza a Alice, a RainhaCopas, os bolinhos, as cartinhas e os corações:
        self.grupo_rainha.update()
        self.rainha.grupo_cartinhas.update()
        self.rainha.grupo_coracoes.update()
        self.grupo_alice.update(lista_eventos)
        self.alice.grupo_bolinhos.update()
        
        # Verifica colisão entre Alice e Rainha e dá uma repulsão na garota:
        if verifica_colisao(self.rainha, self.alice):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000 and not self.alice.pulando:
                self.alice.vidas -= 1
                self.alice.t0_pular_rainha = pygame.time.get_ticks()
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                self.alice.colidindo_rainha = True

        # Verifica colisão entre a Alice e as cartinhas e os corações:
        if pygame.sprite.spritecollide(self.alice, self.rainha.grupo_cartinhas, True, pygame.sprite.collide_mask):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                self.alice.vidas -= 1
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                if not self.canal_dano.get_busy():
                    self.canal_dano.play(SOM_ALICE_DANO, loops=0)
        if pygame.sprite.spritecollide(self.alice, self.rainha.grupo_coracoes, True, pygame.sprite.collide_mask):
            if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                self.alice.vidas -= 1
                self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                if not self.canal_dano.get_busy():
                    self.canal_dano.play(SOM_ALICE_DANO, loops=0)
        
        # Verifica colisão entre os inimigos (RainhaCopas, cartinhas e corações) e os bolinhos:
        if pygame.sprite.spritecollide(self.rainha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
            self.rainha.vidas -= 1
            if not self.canal_acertou.get_busy():
                self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha.grupo_cartinhas, True, True, pygame.sprite.collide_mask):
            if not self.canal_acertou.get_busy():
                self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha.grupo_coracoes, True, True, pygame.sprite.collide_mask):
            if not self.canal_acertou.get_busy():
                self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        
        # Muda de tela quando a RainhaCopas morre:
        if self.rainha.vidas <= 0:
            self.canal_0.stop()
            self.tela_atual = "TelaVitoria"
            self.nivel = 1
            self.dano = 30

        # Termina o jogo quando a Alice morre:
        if self.alice.vidas <= 0:
            self.canal_0.stop()
            self.tela_atual = "TelaGameOver"
            self.nivel = 0
            self.dano = 30 - self.rainha.vidas

        # Caso a cartinha esteja viva, rotaciona e movimenta elas:
        for cartinha in self.rainha.grupo_cartinhas:
            if cartinha.vivo == "Vivo":
                cartinha.movimentar_acelerando()
                cartinha.rotacionar()

        # Atualizando os textos de vidas:
        self.texto_vidas = FONTE_CORACAO.render(CORACAO * self.alice.vidas, True, VERMELHO)
        self.texto_vidas_perdidas = FONTE_CORACAO.render(CORACAO * (5 - self.alice.vidas), True, BRANCO)

        return True
    
    