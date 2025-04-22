# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *

class TelaInicial:
    """ 
    Representa a tela que mostra ao jogador a opção de instruções e início de jogo.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        proxima_tela (str): Representa a próxima tela.
        t0 (int): Tempo em que a Tela é iniciada.
        fundo (Surface): Imagem de fundo.
        canal_0 (Channel): Canal utilizado para a música de fundo.
    """

    def __init__(self) -> None:
        """ 
        Inicializa uma instância da classe TelaInicial. 

        Returns:
            None:
        """
        self.tela_atual = "TelaInicial"
        self.proxima_tela = "TelaCoelho"
        self.t0 = pygame.time.get_ticks()
        self.fundo = FUNDO_TELA_INICAL[0]
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

        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            self.canal_0.play(MUSICA_FUNDO_ALICE, loops=-1)
        
        # Verifica eventos de troca de tela ou saída do jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.canal_0.stop()
                self.tela_atual = "Sair"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.canal_0.stop()
                    self.tela_atual = "Sair" 
                
            if evento.type == pygame.JOYAXISMOTION:
                if evento.axis == 1:
                    if evento.value < - 0.8:
                        self.proxima_tela = "TelaCoelho"
                        self.fundo = FUNDO_TELA_INICAL[0]
                    if evento.value > 0.8:
                        self.proxima_tela = "TelaInstrucoes"
                        self.fundo = FUNDO_TELA_INICAL[1]
            if evento.type == pygame.JOYBUTTONDOWN:
                if evento.button == 0:
                    self.tela_atual = self.proxima_tela
                    if self.proxima_tela == "TelaCoelho":
                        self.canal_0.stop()


        return True
    
    