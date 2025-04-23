# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *
from Classes.Alice.AliceRainhaVermelha import AliceRainhaVermelha
from Classes.PlataformaRainha import PlataformaRainha
from Classes.PlataformaRei import PlataformaRei
from Classes.PlataformaXadrez import PlataformaXadrez
from Classes.RainhaVermelha import RainhaVermelha
from Classes.ReiVermelho import ReiVermelho

class TelaRainhaVermelha:
    """ 
    Representa a tela da Fase 3: Rainha Vermelha.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        dano (int): O dano causado pelo jogador.
        tempo_terminou (int): O tempo em que o jogador termina o jogo.
        t0 (int): O tempo em que a Tela é iniciada.
        grupo_alice (Group): Grupo de sprites da Alice.
        alice (AliceRainhaVermelha): Instância de AliceRainhaVermelha.
        grupo_plataforma (Group): Grupo de sprites da Plataforma de Xadrez.
        grupo_plataforma_rainha (Group): Grupo de sprites da Plataforma da Rainha.
        plataforma_rainha (PlataformaRainha): Instância da PlataformaRainha.
        grupo_plataforma_rei (Group): Grupo de sprites da Plataforma do Rei.
        plataforma_rei (PlataformaRei): Instância da PlataformaRei.
        grupo_rainha (Group): Grupo de sprites da RainhaVermelha.
        rainha_vermelha (RainhaVermelha): Instância da RainhaVermelha.
        grupo_rei (Group): Grupo de sprites do Rei.
        rei_vermelho (ReiVermelho): Instância do ReiVermelho.
        canal_0 (Channel): Canal utilizado para a música de fundo.
        canal_dano (Channel): Canal utilizado para a Alice levando dano.
        canal_acertou (Channel): Canal utilizado para Alice acertando um alvo.
        texto_vidas (Surface): Texto de vidas da Alice.
        texto_vidas_perdidas (Surface): Texto de vidas perdidas da Alice.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaRainhaVermelha. 

        Returns:
            None:
        """
        self.tela_atual = "TelaRainhaVermelha"
        self.nivel = 2
        self.dano = 0
        self.tempo_terminou = 0
        self.t0 = pygame.time.get_ticks()
        self.grupo_alice = pygame.sprite.Group()
        self.alice = AliceRainhaVermelha(LARGURA_TELA//2, ALTURA_TELA//2 - 110)
        self.grupo_alice.add(self.alice)
        self.grupo_plataforma = pygame.sprite.Group()
        self.grupo_plataforma.add(PlataformaXadrez())
        self.grupo_plataforma_rainha = pygame.sprite.Group()
        self.plataforma_rainha = PlataformaRainha()
        self.grupo_plataforma_rainha.add(self.plataforma_rainha)
        self.grupo_plataforma_rei = pygame.sprite.Group()
        self.plataforma_rei = PlataformaRei()
        self.grupo_plataforma_rei.add(self.plataforma_rei)
        self.grupo_rainha = pygame.sprite.Group()
        self.rainha_vermelha = RainhaVermelha(LARGURA_TELA - 210, 68, self.alice)
        self.grupo_rainha.add(self.rainha_vermelha)
        self.grupo_rei = pygame.sprite.Group()
        self.rei_vermelho = ReiVermelho(50, 70)
        self.grupo_rei.add(self.rei_vermelho)
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

        # Desenhando a tela de fundo e a RainhaBranca:
        window.fill(BRANCO)
        window.blit(IMAGEM_FUNDO_RAINHA_VERMELHA, (0, 0))
        window.blit(IMAGEM_RAINHA_BRANCA, (LARGURA_TELA//2 - IMAGEM_RAINHA_BRANCA.get_width()//2, 0))

        # Desenhando personagens e plataformas:
        self.grupo_plataforma.draw(window)
        self.grupo_plataforma_rainha.draw(window)
        self.grupo_plataforma_rei.draw(window)
        self.grupo_rainha.draw(window)
        self.grupo_rei.draw(window)
        self.rainha.grupo_livros.draw(window)
        self.rei.grupo_pecas.draw(window)
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
            self.canal_0.play(MUSICA_FUNDO_RAINHA_VERMELHA, loops=-1)
        
        # Verifica eventos de troca de tela ou saída do jogo:
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.tela_atual = "Sair"
                self.canal_0.stop()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.tela_atual = "Sair"
                    self.canal_0.stop()

        # Atualiza a Alice, a RainhaVermelha, o Reivermelho, os bolinhos, as peças e os livros:            
        self.grupo_plataforma.update()
        self.grupo_plataforma_rainha.update()
        self.grupo_plataforma_rei.update()
        self.grupo_rainha.update()
        self.grupo_rei.update()
        self.rainha.grupo_livros.update()
        self.rei.grupo_pecas.update()
        self.alice.update(lista_eventos)
        self.alice.grupo_bolinhos.update()
        

        if len(self.grupo_rainha) > 0:

            # Verifica colisão entre a Alice e os livros:
            if pygame.sprite.spritecollide(self.alice, self.rainha_vermelha.grupo_livros, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                    if not self.canal_dano.get_busy():
                        self.canal_dano.play(SOM_ALICE_DANO, loops=0)

            # Verifica colisão entre a RainhaVermelha e os bolinhos:
            if pygame.sprite.spritecollide(self.rainha_vermelha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rainha_vermelha.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verifica colisão entre a Plataforma da Rainha e os bolinhos:
            if pygame.sprite.spritecollide(self.plataforma_rainha, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rainha_vermelha.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)

            # Verifica colisão entre os bolinhos e os livros:
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rainha_vermelha.grupo_livros, True, True, pygame.sprite.collide_mask):
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)

        if len(self.grupo_rei) > 0:

            # Verifica colisão entre Alice e as peças de xadrez:
            if pygame.sprite.spritecollide(self.alice, self.rei_vermelho.grupo_pecas, True, pygame.sprite.collide_mask):
                if (pygame.time.get_ticks() - self.alice.t0_ultimo_dano) > 1000:
                    self.alice.vidas -= 1
                    self.alice.t0_ultimo_dano = pygame.time.get_ticks()
                    if not self.canal_dano.get_busy():
                        self.canal_dano.play(SOM_ALICE_DANO, loops=0)
            
            # Verifica colisão entre o ReiVermelho e os Bolinhos:
            if pygame.sprite.spritecollide(self.rei_vermelho, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rei_vermelho.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)

            # Verifica colisão entre a Plataforma do Rei e os bolinhos:
            if pygame.sprite.spritecollide(self.plataforma_rei, self.alice.grupo_bolinhos, True, pygame.sprite.collide_mask):
                self.rei_vermelho.vidas -= 1
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
            
            # Verifica a colisão entre os bolinhos e as peças de xadrez:
            if pygame.sprite.groupcollide(self.alice.grupo_bolinhos, self.rei_vermelho.grupo_pecas, True, True, pygame.sprite.collide_mask):
                if not self.canal_acertou.get_busy():
                    self.canal_acertou.play(SOM_ALICE_ACERTOU, loops=0)
        
        # Muda de tela quando a RainhaVermelha e o Rei morrem:
        if len(self.grupo_rainha) + len(self.grupo_rei) == 0:
            self.tela_atual = "TelaVitoria"
            self.tempo_terminou = pygame.time.get_ticks()//1000
            self.nivel = 3
            self.dano = 40
        
        # Termina o jogo quando a Alice morre:
        if self.alice.vidas <= 0:
            self.tela_atual = "TelaGameOver"
            self.nivel = 2
            self.dano = 20 - self.rainha_vermelha.vidas + 20 - self.rei_vermelho.vidas

        # Atualizando os textos de vidas:
        self.texto_vidas = FONTE_CORACAO.render(CORACAO * self.alice.vidas, True, VERMELHO)
        self.texto_vidas_perdidas = FONTE_CORACAO.render(CORACAO * (5 - self.alice.vidas), True, BRANCO)

        return True
    
    