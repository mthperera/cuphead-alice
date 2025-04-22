# 1. Módulos de terceiros (pip)
import pygame
from pygame.surface import Surface

# 2. Módulos locais
from constantes import *

class TelaCartas:
    """ 
    Representa a tela que mostra ao jogador a próxima fase que ele vai enfrentar.

    Attributes:
        tela_atual (str): A tela atual (a qual pode ser atualizada).
        nivel (int): O nível do jogador.
        dict_cartas_viradas (dict): Mapeamento das imagens das cartas viradas e suas posições.
        canal_0 (Channel): Canal utilizado para a música de fundo.
    """

    def __init__(self, nivel : int) -> None:
        """ 
        Inicializa uma instância da classe TelaCartas. 
        
        Args:
        nivel (int): O nível do jogador.

        Returns:
            None:
        """
        self.tela_atual = "TelaCartas"
        self.t0 = pygame.time.get_ticks()
        self.nivel = nivel
        self.dict_cartas_viradas = {
            LISTA_CARTA_VIRADA[0] : (9, 55),
            LISTA_CARTA_VIRADA[1] : (468, 55),
            LISTA_CARTA_VIRADA[2] : (880, 55),
        }
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
        window.blit(FUNDO_CARTAS, (0, 0))

        # Desenhando as cartas viradas de acordo com o nível:
        for i in range(self.nivel):
            window.blit(LISTA_CARTA_VIRADA[i], self.dict_cartas_viradas[LISTA_CARTA_VIRADA[i]])

        pygame.display.flip()

    def atualiza_estado(self) -> bool:
        """
        Atualiza as informações da tela, tais como música, cartas viradas e eventos.

        Returns:
            bool: 
                - True se continuar na tela.
        """

        # Toca a música de fundo caso já não esteja tocando:
        if not self.canal_0.get_busy():
            MUSICA_FUNDO_CARTAS.set_volume(1.0)
            self.canal_0.play(MUSICA_FUNDO_CARTAS, loops=-1)

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
                    if self.nivel == 0:
                        self.tela_atual = "TelaRainhaCopas"
                    elif self.nivel == 1:
                        self.tela_atual = "TelaTweedle"
                    elif self.nivel == 2:
                        self.tela_atual = "TelaRainhaVermelha"
                    elif self.nivel == 3:
                        self.tela_atual = "TelaRanking"
                    self.canal_0.stop()

        return True
    
    