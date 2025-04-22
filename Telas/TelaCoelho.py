# 1. Módulos da biblioteca padrão
from random import choice

# 2. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 3. Módulos locais
from constantes import *
from Classes.Alice.AliceCoelho import AliceCoelho
from Classes.Coelho import Coelho


class TelaCoelho:
    """ 
    Representa a tela do coelho e o buraco mágico.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        coelho (Coelho): Instância de Coelho.
        t0 (int): O tempo em que a Tela é iniciada.
        fundo (Surface): Imagem de fundo.
        canal_0 (Channel): Canal utilizado para a música de fundo.
        grupo_alice (Group): Grupo de sprites da Alice.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaCoelho. 

        Returns:
            None:
        """
        self.tela_atual = "TelaCoelho"
        self.nivel = 0
        self.coelho = Coelho()
        self.t0 = pygame.time.get_ticks()
        self.fundo = choice(LISTA_FUNDO_COELHO)
        self.canal_0 = pygame.mixer.Channel(0)
        self.grupo_alice = pygame.sprite.Group()
        self.grupo_alice.add(AliceCoelho(400, ALTURA_TELA - 140))

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo e os personagens.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill(BRANCO)
        window.blit(self.fundo, (0, 0))

        # Desenhando os personagens:
        self.coelho.desenhar(window)
        self.grupo_alice.draw(window)

        pygame.display.flip()

    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como música, eventos e personagens.

        Returns:
            bool: 
                - True se continuar na tela.
        """
        
        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            self.canal_0.play(MUSICA_FUNDO_COELHO, loops=-1)
        
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


        # Movimenta personagens:
        self.coelho.movimentar()
        self.grupo_alice.update(lista_eventos)
        

        # Realiza o salto do coelho:
        if self.coelho.pos_x > 2*LARGURA_TELA/5 and not self.coelho.pulo:
            self.coelho.pulo = True
            self.coelho.pos_y -= 30
            self.coelho.i = 0
            self.coelho.t0_pulo = pygame.time.get_ticks()
        
        # Realiza a troca de telas quando a Alice entra no buraco:
        for alice in self.grupo_alice:
            if alice.rect.x > 5.5 * LARGURA_TELA // 9:
                self.tela_atual = "TelaCartas"
                self.canal_0.stop()

        # Anima o coelho:
        if not self.coelho.pulo:
            self.coelho.animar()
        else:
            self.coelho.pular()


        return True
    
