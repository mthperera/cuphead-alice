# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *

class TelaVitoria:
    """ 
    Representa a tela que mostra ao jogador a Alice comemorando após ganhar.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        t0 (int): O tempo em que a Tela é iniciada.
        fundo (Surface): Mapeamento das imagens das cartas viradas e suas posições.
        canal_0 (Channel): Canal utilizado para a música de fundo.
    """

    def __init__(self, nivel : int) -> None:
        """ 
        Inicializa uma instância da classe TelaVitoria. 
        
        Args:
        nivel (int): O nível do jogador.

        Returns:
            None:
        """
        self.tela_atual = "TelaVitoria"
        self.t0 = pygame.time.get_ticks()
        self.nivel = nivel
        self.fundo = FUNDO_VITORIA[self.nivel - 1]
        self.canal_0 = pygame.mixer.Channel(0)

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo e as cartas das fases.

        Args:
            window (Surface) : Janela na qual tudo será desenhado.
        
        Returns:
            None:
        """

        # Desenhando a tela de fundo:
        window.fill(BRANCO)
        window.blit(self.fundo, (0, 0))

        pygame.display.flip()
    
    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como música e eventos.

        Returns:
            bool: 
                - True se continuar na tela.
        """

        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            self.canal_0.play(MUSICA_FUNDO_GAMEOVER, loops=-1)

        # Verifica eventos de troca de tela ou saída do jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair"
            
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.tela_atual = "TelaCartas"


        return True
    
    