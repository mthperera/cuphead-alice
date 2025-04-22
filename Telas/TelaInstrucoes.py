# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *

class TelaInstrucoes:
    """ 
    Representa a tela de instruções.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        t0 (int): Tempo em que a Tela é iniciada.
        fundo (Surface): Imagem de fundo.
        canal_0 (Channel): Canal utilizado para a música de fundo.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaInstrucoes. 

        Returns:
            None:
        """

        self.tela_atual = "TelaInstrucoes"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_INSTRUCOES
        self.canal_0 = pygame.mixer.Channel(0)

    def desenha(self, window : Surface) -> None:
        """
        Desenha o fundo.

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
                if evento.button == 1:
                    self.tela_atual = "TelaInicial"


        return True
    
    