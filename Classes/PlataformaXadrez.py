# 1. Módulos da biblioteca padrão
from math import cos

# 2. Módulos de terceiros (pip)
import pygame

# 3. Módulos locais
from constantes import *

class PlataformaXadrez(pygame.sprite.Sprite):
    """
    Plataforma na qual a Alice apoia:

    Attributes:
        pos_x (int): Posição horizontal da Plataforma de Xadrez.
        pos_y (int): Posição vertical inicial da Plataforma de Xadrez.
        t0 (int): O tempo em que a Plataforma foi criada.
        image (Surface): Imagem da Plataforma de Xadrez.
        mask (Mask): Mask inicial da Plataforma de Xadrez.
        rect (Rect): Rect inicial da Plataforma de Xadrez.
    """
    def __init__(self):
        """
        Inicializa uma instância da classe PlataformaXadrez.

        Returns:
            None:
        """
        super().__init__()
        self.image = IMAGEM_PLATAFORMA_XADREZ   
        self.pos_x = (LARGURA_TELA - self.image.get_width())//2
        self.pos_y = (ALTURA_TELA - self.image.get_height())//2 + 145
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.t0 = pygame.time.get_ticks()
    
    def movimentar(self) -> None:
        """
        Movimenta a plataforma em MHS vertical.

        Returns:
            None:
        """

        # Realizando MHS vertical:
        self.rect.y = self.pos_y + 10 * cos((pygame.time.get_ticks() - self.t0)/1000)

    def update(self) -> None:
        """
        Atualiza a Plataforma de Xadrez.

        Returns:
            None:
        """
        
        # Movimenta a Plataforma de Xadrez:
        self.movimentar()

        # Atualiza a mask da Plataforma de Xadrez:
        self.mask = pygame.mask.from_surface(self.image)